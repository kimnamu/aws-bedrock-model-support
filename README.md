# AWS Bedrock Model Availability Tracker

Track AWS Bedrock model availability across regions.

## Model Availability

<!-- BEDROCK_AVAILABILITY_START -->

![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--1--29-blue)
 ![Regions](https://img.shields.io/badge/Regions-14-green)
 ![Providers](https://img.shields.io/badge/Providers-17-orange)

### Last Updated

| UTC | PST (US West) | KST (Korea) |
|:---:|:---:|:---:|
| 2026-01-29 19:10 | 2026-01-29 11:10 | 2026-01-30 04:10 |

## Table of Contents

| Provider | Models | Regions |
|:---------|-------:|--------:|
| [AI21 Labs](#ai21-labs) | 2 | 1 |
| [Amazon](#amazon) | 32 | 14 |
| [Anthropic](#anthropic) | 31 | 14 |
| [Cohere](#cohere) | 8 | 14 |
| [DeepSeek](#deepseek) | 2 | 6 |
| [Google](#google) | 3 | 8 |
| [Luma AI](#luma-ai) | 1 | 1 |
| [Meta](#meta) | 19 | 9 |
| [MiniMax](#minimax) | 1 | 8 |
| [Mistral AI](#mistral-ai) | 13 | 12 |
| [Moonshot AI](#moonshot-ai) | 1 | 6 |
| [NVIDIA](#nvidia) | 3 | 8 |
| [OpenAI](#openai) | 4 | 9 |
| [Qwen](#qwen) | 6 | 9 |
| [Stability AI](#stability-ai) | 16 | 3 |
| [TwelveLabs](#twelvelabs) | 3 | 14 |
| [Writer](#writer) | 2 | 3 |

---

<details>
<summary><h3 id="ai21-labs">AI21 Labs (2 models, 1 regions)</h3></summary>

| Model | us-east-1 |
|:------|:---:|
| Jamba 1.5 Large | ✅ |
| Jamba 1.5 Mini | ✅ |

</details>

<details>
<summary><h3 id="amazon">Amazon (32 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Nova 2 Sonic | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova 2 Lite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova 2 Lite (256k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova 2 Multimodal Embed | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Premier (8k) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Premier (20k) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Premier (1000k) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Premier (mm) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Premier | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Pro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Pro (24k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Pro (300k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Lite (24k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Lite (300k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Lite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Micro (24k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Micro (128k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Micro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Canvas | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Reel v1.1 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Reel | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Sonic | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Text G1 Large | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text v2 (8k) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text v2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Titan Embed Text (8k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed G1 Text | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Image | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Titan Embed Image | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Titan Image Generator v2 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Amazon Rerank | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="anthropic">Anthropic (31 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Claude Opus 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Sonnet 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Haiku 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Opus 4.1 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Opus 4 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Sonnet 4 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.7 Sonnet | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.5 Sonnet | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.5 Sonnet v2 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.5 Sonnet v2 (18k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet v2 (51k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet v2 (200k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet (18k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet (51k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet (200k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Haiku | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Opus (12k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Opus (28k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Opus (200k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Opus | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Sonnet (28k) | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3 Sonnet (200k) | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Claude 3 Sonnet | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude 3 Haiku (48k) | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| Claude 3 Haiku (200k) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Claude 3 Haiku | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude 2.1 (18k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2.1 (200k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2 (18k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2 (100k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Instant (100k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="cohere">Cohere (8 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Command R+ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Command R | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Embed v4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Embed English v3 (512) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Embed English v3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Embed Multilingual v3 (512) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Embed Multilingual v3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Rerank v3.5 | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="deepseek">DeepSeek (2 models, 6 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-2 | ap-northeast-1 | ap-south-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| DeepSeek R1 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| DeepSeek V3 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="google">Google (3 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Gemma 3 27B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma 3 12B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma 3 4B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="luma-ai">Luma AI (1 models, 1 regions)</h3></summary>

| Model | us-west-2 |
|:------|:---:|
| Luma Ray v2 | ✅ |

</details>

<details>
<summary><h3 id="meta">Meta (19 models, 9 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-south-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Llama 4 Maverick 17B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 4 Scout 17B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.3 70B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.3 70B (128k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 90B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 90B (128k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 11B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 11B (128k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 3B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Llama 3.2 3B (128k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 1B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Llama 3.2 1B (128k) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 405B | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 70B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 70B (128k) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 8B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 8B (128k) | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3 70B | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Llama 3 8B | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |

</details>

<details>
<summary><h3 id="minimax">MiniMax (1 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MiniMax M2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="mistral-ai">Mistral AI (13 models, 12 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mistral Large 3 675B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Pixtral Large | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Mistral Large | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral Large 2 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Magistral Small | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Mistral Small | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Voxtral Small 24B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Voxtral Mini 3B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Mixtral 8x7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral 7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Ministral 14B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ministral 8B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ministral 3B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="moonshot-ai">Moonshot AI (1 models, 6 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| Kimi K2 Thinking | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="nvidia">NVIDIA (3 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Nemotron Nano 12B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nemotron Nano 9B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Nemotron Nano 30B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="openai">OpenAI (4 models, 9 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| GPT OSS 120B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GPT OSS 20B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GPT OSS Safeguard 120B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GPT OSS Safeguard 20B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="qwen">Qwen (6 models, 9 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Qwen3 Coder 480B | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Qwen3 235B | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Qwen3 VL 235B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 Next 80B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 Coder 30B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 32B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="stability-ai">Stability AI (16 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| SD3.5 Large | ❌ | ❌ | ✅ |
| Stable Image Ultra v1.1 | ❌ | ❌ | ✅ |
| Stable Image Core v1.1 | ❌ | ❌ | ✅ |
| Creative Upscale | ✅ | ✅ | ✅ |
| Remove Background | ✅ | ✅ | ✅ |
| Image Control Sketch | ✅ | ✅ | ✅ |
| Conservative Upscale | ✅ | ✅ | ✅ |
| Search Recolor | ✅ | ✅ | ✅ |
| Fast Upscale | ✅ | ✅ | ✅ |
| Image Erase Object | ✅ | ✅ | ✅ |
| Image Control Structure | ✅ | ✅ | ✅ |
| Outpaint | ✅ | ✅ | ✅ |
| Image Inpaint | ✅ | ✅ | ✅ |
| Style Guide | ✅ | ✅ | ✅ |
| Style Transfer | ✅ | ✅ | ✅ |
| Search Replace | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="twelvelabs">TwelveLabs (3 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Pegasus 1.2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Marengo Embed 3.0 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Marengo Embed 2.7 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="writer">Writer (2 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| Palmyra X5 | ✅ | ✅ | ✅ |
| Palmyra X4 | ✅ | ✅ | ✅ |

</details>


---

## Summary

| Metric | Value |
|--------|-------|
| Total Models | **147** |
| Total Regions | **14** |
| Providers | **17** |

### Provider Breakdown

| Provider | Models | Regions |
|----------|--------|---------|
| AI21 Labs | 2 | 1 |
| Amazon | 32 | 14 |
| Anthropic | 31 | 14 |
| Cohere | 8 | 14 |
| DeepSeek | 2 | 6 |
| Google | 3 | 8 |
| Luma AI | 1 | 1 |
| Meta | 19 | 9 |
| MiniMax | 1 | 8 |
| Mistral AI | 13 | 12 |
| Moonshot AI | 1 | 6 |
| NVIDIA | 3 | 8 |
| OpenAI | 4 | 9 |
| Qwen | 6 | 9 |
| Stability AI | 16 | 3 |
| TwelveLabs | 3 | 14 |
| Writer | 2 | 3 |

<!-- BEDROCK_AVAILABILITY_END -->

## Usage

This repository is automatically updated every hour.

## License

MIT License
