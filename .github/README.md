# Amazon Bedrock Model Explorer

Which Bedrock model ID or inference profile to call from your region, what each model accepts on the Converse API, and what is retiring.

Open the explorer at https://kimnamu.github.io/aws-bedrock-model-support/ (for example, [Claude Opus 5.5 called from eu-central-1](https://kimnamu.github.io/aws-bedrock-model-support/#model=anthropic.claude-opus-5-5&region=eu-central-1)).

The data comes from the public `ListFoundationModels` and `ListInferenceProfiles` APIs in 17 regions, plus one small Converse call per active text model each day in us-east-1.

| File | What it holds | Refreshed |
|---|---|---|
| [catalog.json](https://kimnamu.github.io/aws-bedrock-model-support/data/catalog.json) | every model and inference profile, with the ID to call from each region | hourly check, committed on change |
| [probes.json](https://kimnamu.github.io/aws-bedrock-model-support/data/probes.json) | Converse results for each active text model: system, temperature, top_p, stop_sequences, tool choice (auto and forced), cache point, prefill | daily |
| [history.json](https://kimnamu.github.io/aws-bedrock-model-support/data/history.json) | region additions and removals since 2026-01-26 | hourly check, committed on change |
| [availability.json](https://raw.githubusercontent.com/kimnamu/aws-bedrock-model-support/main/docs/data/availability.json) | the raw hourly listing behind the table in the root README | hourly |

```sh
curl -s https://kimnamu.github.io/aws-bedrock-model-support/data/catalog.json \
  | jq '.models["anthropic.claude-opus-5-5"].profiles'
```

The hourly table in the [root README](../README.md) is the raw `ListFoundationModels` listing, so a checkmark there can still need an inference profile. The explorer and `catalog.json` show the ID that works from each region.

A probe result says whether the API accepted or rejected a parameter. It does not show that the parameter changed the output.

Independent community project, not an AWS page. Issues are welcome.
