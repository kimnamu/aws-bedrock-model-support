#!/usr/bin/env python3
"""Build docs/data/catalog.json from the Bedrock control plane.

For every region that answers, calls ListFoundationModels and ListInferenceProfiles
(SYSTEM_DEFINED) and keeps only public catalog facts: model metadata, how each model
can be invoked per region (on-demand vs inference profile), and where each
cross-region profile can be called from and routes to.

Auth: AWS_BEARER_TOKEN_BEDROCK (a Bedrock API key). Stdlib only.
Account-scoped fields (profile ARNs carry the caller's account ID) are dropped,
and the output is checked for any 12-digit number before it is written.

usage: python3 src/catalog.py [out.json]
"""
import datetime, json, os, re, sys, urllib.error, urllib.parse, urllib.request

REGIONS = [  # commercial regions; opt-in regions that return 403 are skipped and reported
    "us-east-1", "us-east-2", "us-west-1", "us-west-2", "ca-central-1", "sa-east-1",
    "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "eu-south-1", "eu-south-2", "eu-central-2",
    "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-south-1", "ap-south-2",
    "ap-southeast-1", "ap-southeast-2", "ap-southeast-3", "ap-southeast-4", "ap-southeast-5", "ap-southeast-7",
    "ap-east-2", "ca-west-1", "il-central-1", "me-central-1", "mx-central-1",
]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "data", "catalog.json")


def get(region, path):
    req = urllib.request.Request(f"https://bedrock.{region}.amazonaws.com/{path}",
                                 headers={"Authorization": "Bearer " + os.environ["AWS_BEARER_TOKEN_BEDROCK"]})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def profiles(region):
    out, token = [], None
    while True:
        q = "inference-profiles?maxResults=1000&type=SYSTEM_DEFINED" + (f"&nextToken={urllib.parse.quote(token)}" if token else "")
        d = get(region, q)
        out += d.get("inferenceProfileSummaries", [])
        token = d.get("nextToken")
        if not token:
            return out


def arn_region(arn):
    return arn.split(":")[3]


def reasoning(schema):
    """additionalRequestFieldsSchema is a JSON string; pull the effort/reasoning enum and the sampling flag."""
    try:
        s = json.loads(schema or "{}")
    except ValueError:
        return None, [], False
    hide = bool(s.pop("hideSamplingParameter", False))
    for key, v in s.items():
        node = v.get("effort", v) if isinstance(v, dict) else {}
        if isinstance(node, dict) and node.get("enum"):
            path = f"{key}.effort" if "effort" in v else key
            return path, node["enum"], hide
    return None, [], hide


def model_facts(m):
    cv, api, feat, life = m.get("converse") or {}, m.get("inferenceAPIsSupported") or {}, m.get("featuresSupported") or {}, m.get("modelLifecycle") or {}
    rpath, levels, hide = reasoning(cv.get("additionalRequestFieldsSchema"))
    return {
        "name": m.get("modelName"), "provider": m.get("providerName"), "family": m.get("modelFamily"),
        "input": m.get("inputModalities") or [], "output": m.get("outputModalities") or [],
        "status": life.get("status"), "released": life.get("startOfLifeTime"), "legacy": life.get("legacyTime"),
        "extended": life.get("publicExtendedAccessTime"), "eol": life.get("endOfLifeTime"),
        "max_tokens": cv.get("maxTokensMaximum"), "default_max_tokens": cv.get("maxTokensDefault"),
        "system_role": cv.get("systemRoleSupported"), "images": cv.get("userImageTypesSupported") or [],
        "documents": cv.get("userDocumentTypesSupported") or [], "videos": cv.get("userVideoTypesSupported") or [],
        "reasoning_field": rpath, "reasoning_levels": levels, "no_sampling": hide,
        "streaming": bool(m.get("responseStreamingSupported")),
        "converse": bool((api.get("converse") or {}).get("sync")),
        "openai_chat": bool(api.get("openAiChatCompletions")), "openai_responses": bool(api.get("openAiResponses")),
        "prompt_caching": bool(feat.get("promptCaching")), "count_tokens": bool(feat.get("countTokens")),
        "batch": bool((feat.get("batchInference") or {}).get("inRegion") or (feat.get("batchInference") or {}).get("crossRegion")),
        "guardrails": bool(m.get("guardrailsSupported")), "customization": m.get("customizationsSupported") or [],
    }


def build():
    models, prof, ok, skipped = {}, {}, [], {}
    for r in REGIONS:
        try:
            fms = get(r, "foundation-models").get("modelSummaries", [])
            ips = profiles(r)
        except urllib.error.HTTPError as e:
            skipped[r] = e.code
            continue
        except (urllib.error.URLError, TimeoutError) as e:
            skipped[r] = str(getattr(e, "reason", e))[:40]
            continue
        ok.append(r)
        for m in fms:
            entry = models.setdefault(m["modelId"], {**model_facts(m), "regions": {}})
            entry["regions"][r] = sorted(m.get("inferenceTypesSupported") or [])
        for p in ips:
            e = prof.setdefault(p["inferenceProfileId"], {"name": p.get("inferenceProfileName"), "from": [], "to": set(), "models": set()})
            e["from"].append(r)
            for x in p.get("models") or []:
                if arn_region(x["modelArn"]):          # global profiles also list a region-less ARN (arn:aws:bedrock:::...) meaning "any region"
                    e["to"].add(arn_region(x["modelArn"]))
                e["models"].add(x["modelArn"].rsplit("/", 1)[-1])
    for pid, e in prof.items():
        e["to"], e["models"] = sorted(e["to"]), sorted(e["models"])
        e["scope"] = pid.split(".", 1)[0]
        for mid in e["models"]:
            if mid in models:
                models[mid].setdefault("profiles", []).append(pid)
    return {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "regions": ok, "skipped_regions": skipped, "models": models, "profiles": prof,
    }


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else OUT
    data = build()
    text = json.dumps(data, indent=1, sort_keys=True)
    assert not re.search(r"(?<!\d)\d{12}(?!\d)", text), "12-digit number in output (account ID?) - refusing to write"
    old = None
    if os.path.exists(out):
        with open(out) as f:
            old = json.load(f)
    if old and {k: v for k, v in old.items() if k != "generated_at"} == {k: v for k, v in data.items() if k != "generated_at"}:
        print("catalog: no change")
        return 0
    with open(out + ".tmp", "w") as f:
        f.write(text + "\n")
    os.replace(out + ".tmp", out)
    print(f"catalog: {len(data['models'])} models, {len(data['profiles'])} profiles, {len(data['regions'])} regions (skipped {len(data['skipped_regions'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
