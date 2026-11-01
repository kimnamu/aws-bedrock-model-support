#!/bin/sh
# Rebuild catalog / history / probes and push them if they changed.
#   hourly: refresh.sh          (catalog + history)
#   daily:  refresh.sh probe    (also runs the parameter probes)
# Needs AWS_BEARER_TOKEN_BEDROCK. The hourly tracker commits availability.json at :10, so run this off that minute.
set -eu
cd "$(dirname "$0")/.."
# cron has no shell profile: take the Bedrock API key from Claude Code's settings.json env (same key the pipeline uses)
if [ -z "${AWS_BEARER_TOKEN_BEDROCK:-}" ]; then
  AWS_BEARER_TOKEN_BEDROCK=$(python3 -c 'import json,os;print(json.load(open(os.path.expanduser("~/.claude/settings.json")))["env"]["AWS_BEARER_TOKEN_BEDROCK"])')
  export AWS_BEARER_TOKEN_BEDROCK
fi
git pull -q --rebase --autostash   # a human editing the clone must not break the hourly job (11-01 10:35 exit 128)
python3 src/catalog.py
python3 src/history.py
[ "${1:-}" = probe ] && python3 src/probe.py
git add docs/data/catalog.json docs/data/history.json docs/data/probes.json 2>/dev/null || true
git diff --cached --quiet && exit 0
git -c user.name="Bedrock Tracker" -c user.email="tracker@example.com" commit -q -m "data: catalog/history/probes $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q || { git pull -q --rebase --autostash && git push -q; }
