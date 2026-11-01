#!/usr/bin/env python3
"""Send tiny Converse requests to every active text model and record what Bedrock accepts.

The API metadata does not say whether a model takes temperature, stop sequences, a forced
tool or a cachePoint, and the answers change over time (GPT-6.1 Sol rejected cachePoint on
2026-10-05 and accepted it on 2026-11-01). So we ask the service. Each probe is one request
with maxTokens 16. A probe "passes" when Bedrock returns a response, "fails" with the
error message it returned. Acceptance is not proof that a feature has an effect.

usage: python3 src/probe.py [catalog.json] [out.json]
"""
import concurrent.futures as cf, datetime, json, os, re, sys, time, urllib.error, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CAT = os.path.join(HERE, "..", "docs", "data", "catalog.json")
OUT = os.path.join(HERE, "..", "docs", "data", "probes.json")
REGION = "us-east-1"
USER = [{"role": "user", "content": [{"text": "Reply with the word pong."}]}]
TOOL = {"tools": [{"toolSpec": {"name": "ping", "description": "Return pong.", "inputSchema": {"json": {"type": "object", "properties": {}}}}}]}
PROBES = {  # name -> extra request fields (merged into the baseline body)
    "system": {"system": [{"text": "Be brief."}]},
    "temperature": {"inferenceConfig": {"maxTokens": 16, "temperature": 0.5}},
    "top_p": {"inferenceConfig": {"maxTokens": 16, "topP": 0.9}},
    "stop_sequences": {"inferenceConfig": {"maxTokens": 16, "stopSequences": ["###"]}},
    "tool_auto": {"toolConfig": {**TOOL, "toolChoice": {"auto": {}}}},
    "tool_forced": {"toolConfig": {**TOOL, "toolChoice": {"any": {}}}},
    "cache_point": {"system": [{"text": "Be brief."}, {"cachePoint": {"type": "default"}}]},
    "prefill": {"messages": USER + [{"role": "assistant", "content": [{"text": "p"}]}]},
}


def converse(model_id, body):
    req = urllib.request.Request(f"https://bedrock-runtime.{REGION}.amazonaws.com/model/{urllib.request.quote(model_id, safe='')}/converse",
                                 data=json.dumps(body).encode(), method="POST",
                                 headers={"Authorization": "Bearer " + os.environ["AWS_BEARER_TOKEN_BEDROCK"], "content-type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                json.load(r)
                return True, ""
        except urllib.error.HTTPError as e:
            try:
                msg = json.load(e).get("message", "")
            except ValueError:
                msg = ""
            if e.code in (429, 503) and attempt < 2:
                time.sleep(4 * (attempt + 1))
                continue
            return False, re.sub(r"(?<!\d)\d{12}(?!\d)", "<account>", f"{e.code} {msg}")[:200]  # ARNs in errors carry the account ID
        except (urllib.error.URLError, TimeoutError) as e:
            return False, f"network {str(getattr(e, 'reason', e))[:80]}"
    return False, "throttled"


def call_id(m):
    if "ON_DEMAND" in (m["regions"].get(REGION) or []):
        return m["id"]
    ps = [p for p in m.get("profiles", []) if p.startswith("us.")] + [p for p in m.get("profiles", []) if p.startswith("global.")]
    return ps[0] if ps else None


def probe_model(m):
    mid = call_id(m)
    base = {"messages": USER, "inferenceConfig": {"maxTokens": 16}}
    ok, err = converse(mid, base)
    if not ok:  # no access, needs a Marketplace agreement, or not a chat model: record and stop
        return m["id"], {"via": mid, "baseline": err}
    res = {}
    for name, extra in PROBES.items():
        res[name] = converse(mid, {**base, **extra})
    return m["id"], {"via": mid, "baseline": "", "results": {k: (v[0], v[1]) for k, v in res.items()}}


def main():
    cat = json.load(open(sys.argv[1] if len(sys.argv) > 1 else CAT))
    out = sys.argv[2] if len(sys.argv) > 2 else OUT
    models = [dict(m, id=i) for i, m in cat["models"].items()
              if m["status"] == "ACTIVE" and m.get("converse") and "TEXT" in m["output"] and "TEXT" in m["input"]]
    models = [m for m in models if call_id(m)]
    rows = {}
    with cf.ThreadPoolExecutor(6) as ex:
        for mid, r in ex.map(probe_model, models):
            rows[mid] = r
    data = {"measured_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "region": REGION,
            "probes": list(PROBES), "models": rows}
    assert not re.search(r"(?<!\d)\d{12}(?!\d)", json.dumps(data)), "12-digit number in output (account ID?) - refusing to write"
    with open(out + ".tmp", "w") as f:
        json.dump(data, f, indent=0, sort_keys=True)
    os.replace(out + ".tmp", out)
    ok = sum(1 for r in rows.values() if not r["baseline"])
    print(f"probe: {len(rows)} models, {ok} answered the baseline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
