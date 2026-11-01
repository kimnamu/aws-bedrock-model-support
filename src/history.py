#!/usr/bin/env python3
"""Build docs/data/history.json from the git history of docs/data/availability.json.

The tracker has committed availability.json every hour since 2026-01, so the history
already records when each model first appeared in each region (and when it left).
This replays those commits and emits one event per change:
  {"t": "2026-10-07T18:10Z", "model": "...", "provider": "...", "added": [regions], "removed": [regions]}
The first snapshot is the baseline and is not reported as additions.

Incremental: history.json keeps the last processed commit; reruns only read newer commits.
usage: python3 src/history.py [out.json]
"""
import datetime, json, os, subprocess, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = "docs/data/availability.json"
OUT = os.path.join(ROOT, "docs", "data", "history.json")


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True, check=True).stdout


def snapshot(rev):
    try:
        d = json.loads(git("show", f"{rev}:{SRC}"))
    except (subprocess.CalledProcessError, ValueError):
        return None
    out = {"__bad__": ("", frozenset(r for r, v in (d.get("regions") or {}).items() if (v or {}).get("error")))}
    for prov, ms in (d.get("providers") or {}).items():
        for mid, v in ms.items():
            regs = v.get("regions") if isinstance(v, dict) else v
            out[mid] = (prov, frozenset(regs or []))
    return out


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else OUT
    hist = {"baseline": None, "last_commit": None, "events": []}
    if os.path.exists(out):
        with open(out) as f:
            hist = json.load(f)
    rng = f"{hist['last_commit']}..HEAD" if hist.get("last_commit") else "HEAD"
    revs = git("log", "--reverse", "--format=%H %ct", rng, "--", SRC).split("\n")
    revs = [r.split(" ", 1) for r in revs if r.strip()]
    if not revs:
        print("history: no new commits")
        return 0
    n0 = len(hist["events"])
    prev = snapshot(hist["last_commit"]) if hist.get("last_commit") else None
    for sha, when in revs:
        cur = snapshot(sha)
        if cur is None or not cur:  # failed collector runs leave empty files; skip instead of "removing" everything
            continue
        t = datetime.datetime.fromtimestamp(int(when), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        if prev is None:
            hist["baseline"] = t
        else:
            bad = cur["__bad__"][1] | prev["__bad__"][1]  # a region that failed to answer is not a change
            for mid in sorted((set(cur) | set(prev)) - {"__bad__"}):
                a = cur.get(mid, (prev.get(mid, ("", None))[0], frozenset()))
                b = prev.get(mid, (a[0], frozenset()))
                added, removed = sorted(a[1] - b[1] - bad), sorted(b[1] - a[1] - bad)
                if added or removed:
                    hist["events"].append({"t": t, "model": mid, "provider": a[0] or b[0], "added": added, "removed": removed})
        if prev is not None:  # carry models of failed regions forward so the next diff compares like with like
            for mid, (pv, regs) in prev.items():
                if mid != "__bad__":
                    keep = regs & cur["__bad__"][1]
                    if keep:
                        cp, cr = cur.get(mid, (pv, frozenset()))
                        cur[mid] = (cp or pv, cr | keep)
        prev, hist["last_commit"] = cur, sha
    if len(hist["events"]) == n0 and os.path.exists(out):  # nothing new: leave the file alone so Pages does not redeploy
        print(f"history: {len(revs)} commits read, no new events")
        return 0
    with open(out + ".tmp", "w") as f:
        json.dump(hist, f, indent=0)
    os.replace(out + ".tmp", out)
    print(f"history: {len(revs)} commits read, {len(hist['events'])} events total")
    return 0


if __name__ == "__main__":
    sys.exit(main())
