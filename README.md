# AWS Bedrock Model Availability Tracker

Track AWS Bedrock model availability across regions.

<!-- NEWS_START -->

## 📰 News

| 날짜 | 유형 | Provider | Model | Regions |
|:-----|:-----|:---------|:------|:--------|
| 2026-02-06 | 🆕 추가 | Anthropic | Claude Opus 4.6 | 14개 리전 |
| 2026-02-06 | 📍 확장 | NVIDIA | Nemotron Nano 30B | eu-west-1 |

<!-- NEWS_END -->

## Model Availability

<!-- BEDROCK_AVAILABILITY_START -->

![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--2--6-blue)
 ![Regions](https://img.shields.io/badge/Regions-14-green)
 ![Providers](https://img.shields.io/badge/Providers-17-orange)

### Last Updated

| UTC | PST (US West) | KST (Korea) |
|:---:|:---:|:---:|
| 2026-02-06 03:10 | 2026-02-05 19:10 | 2026-02-06 12:10 |

## Table of Contents

| Provider | Models | Regions |
|:---------|-------:|--------:|
| [AI21 Labs](#ai21-labs) | 2 | 1 |
| [Amazon](#amazon) | 32 | 14 |
| [Anthropic](#anthropic) | 32 | 14 |
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
<summary><h3 id="anthropic">Anthropic (32 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Claude Opus 4.6 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
| Nemotron Nano 30B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

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
| Total Models | **148** |
| Total Regions | **14** |
| Providers | **17** |

### Provider Breakdown

| Provider | Models | Regions |
|----------|--------|---------|
| AI21 Labs | 2 | 1 |
| Amazon | 32 | 14 |
| Anthropic | 32 | 14 |
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

---

## Model ID Reference

Bedrock API 호출 시 사용하는 Model ID 목록입니다.

<details>
<summary><h3>Anthropic Claude</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Claude Opus 4.6 | `anthropic.claude-opus-4-6-v1` |
| Claude Opus 4.5 | `anthropic.claude-opus-4-5-20251101-v1:0` |
| Claude Sonnet 4.5 | `anthropic.claude-sonnet-4-5-20250929-v1:0` |
| Claude Haiku 4.5 | `anthropic.claude-haiku-4-5-20251001-v1:0` |
| Claude Opus 4.1 | `anthropic.claude-opus-4-1-20250805-v1:0` |
| Claude Opus 4 | `anthropic.claude-opus-4-20250514-v1:0` |
| Claude Sonnet 4 | `anthropic.claude-sonnet-4-20250514-v1:0` |
| Claude 3.7 Sonnet | `anthropic.claude-3-7-sonnet-20250219-v1:0` |
| Claude 3.5 Sonnet v2 | `anthropic.claude-3-5-sonnet-20241022-v2:0` |
| Claude 3.5 Sonnet | `anthropic.claude-3-5-sonnet-20240620-v1:0` |
| Claude 3.5 Haiku | `anthropic.claude-3-5-haiku-20241022-v1:0` |
| Claude 3 Opus | `anthropic.claude-3-opus-20240229-v1:0` |
| Claude 3 Sonnet | `anthropic.claude-3-sonnet-20240229-v1:0` |
| Claude 3 Haiku | `anthropic.claude-3-haiku-20240307-v1:0` |
| Claude 2.1 | `anthropic.claude-v2:1` |
| Claude 2 | `anthropic.claude-v2:0` |
| Claude 2 | `anthropic.claude-v2` |
| Claude Instant | `anthropic.claude-instant-v1` |
| Claude Instant | `anthropic.claude-instant-v1:2` |

</details>

<details>
<summary><h3>Amazon Nova & Titan</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Nova 2 Sonic | `amazon.nova-2-sonic-v1:0` |
| Nova 2 Lite | `amazon.nova-2-lite-v1:0` |
| Nova 2 Multimodal Embed | `amazon.nova-2-multimodal-embeddings-v1:0` |
| Nova Premier | `amazon.nova-premier-v1:0` |
| Nova Pro | `amazon.nova-pro-v1:0` |
| Nova Lite | `amazon.nova-lite-v1:0` |
| Nova Micro | `amazon.nova-micro-v1:0` |
| Nova Canvas | `amazon.nova-canvas-v1:0` |
| Nova Reel v1.1 | `amazon.nova-reel-v1:1` |
| Nova Reel | `amazon.nova-reel-v1:0` |
| Nova Sonic | `amazon.nova-sonic-v1:0` |
| Titan Text Premier | `amazon.titan-text-premier-v1:0` |
| Titan Text Express | `amazon.titan-text-express-v1` |
| Titan Text Lite | `amazon.titan-text-lite-v1` |
| Titan Text G1 Large | `amazon.titan-tg1-large` |
| Titan Embed Text v2 | `amazon.titan-embed-text-v2:0` |
| Titan Embed Text | `amazon.titan-embed-text-v1` |
| Titan Embed Text | `amazon.titan-embed-text-v1:2` |
| Titan Embed G1 Text | `amazon.titan-embed-g1-text-02` |
| Titan Embed Image | `amazon.titan-embed-image-v1` |
| Titan Embed Image | `amazon.titan-embed-image-v1:0` |
| Titan Image Generator v2 | `amazon.titan-image-generator-v2:0` |
| Titan Image Generator | `amazon.titan-image-generator-v1` |
| Amazon Rerank | `amazon.rerank-v1:0` |

</details>

<details>
<summary><h3>Meta Llama</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Llama 4 Maverick 17B | `meta.llama4-maverick-17b-instruct-v1:0` |
| Llama 4 Scout 17B | `meta.llama4-scout-17b-instruct-v1:0` |
| Llama 3.3 70B | `meta.llama3-3-70b-instruct-v1:0` |
| Llama 3.2 90B | `meta.llama3-2-90b-instruct-v1:0` |
| Llama 3.2 11B | `meta.llama3-2-11b-instruct-v1:0` |
| Llama 3.2 3B | `meta.llama3-2-3b-instruct-v1:0` |
| Llama 3.2 1B | `meta.llama3-2-1b-instruct-v1:0` |
| Llama 3.1 405B | `meta.llama3-1-405b-instruct-v1:0` |
| Llama 3.1 70B | `meta.llama3-1-70b-instruct-v1:0` |
| Llama 3.1 8B | `meta.llama3-1-8b-instruct-v1:0` |
| Llama 3 70B | `meta.llama3-70b-instruct-v1:0` |
| Llama 3 8B | `meta.llama3-8b-instruct-v1:0` |
| Llama 2 70B | `meta.llama2-70b-chat-v1` |
| Llama 2 13B | `meta.llama2-13b-chat-v1` |

</details>

<details>
<summary><h3>Mistral AI</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Mistral Large 3 675B | `mistral.mistral-large-3-675b-instruct` |
| Pixtral Large | `mistral.pixtral-large-2502-v1:0` |
| Mistral Large 2 | `mistral.mistral-large-2407-v1:0` |
| Mistral Large | `mistral.mistral-large-2402-v1:0` |
| Magistral Small | `mistral.magistral-small-2509` |
| Mistral Small | `mistral.mistral-small-2402-v1:0` |
| Voxtral Small 24B | `mistral.voxtral-small-24b-2507` |
| Voxtral Mini 3B | `mistral.voxtral-mini-3b-2507` |
| Mixtral 8x7B | `mistral.mixtral-8x7b-instruct-v0:1` |
| Mistral 7B | `mistral.mistral-7b-instruct-v0:2` |
| Ministral 14B | `mistral.ministral-3-14b-instruct` |
| Ministral 8B | `mistral.ministral-3-8b-instruct` |
| Ministral 3B | `mistral.ministral-3-3b-instruct` |

</details>

<details>
<summary><h3>Cohere</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Command R+ | `cohere.command-r-plus-v1:0` |
| Command R | `cohere.command-r-v1:0` |
| Command | `cohere.command-text-v14` |
| Command Light | `cohere.command-light-text-v14` |
| Embed v4 | `cohere.embed-v4:0` |
| Embed English v3 | `cohere.embed-english-v3` |
| Embed English v3 | `cohere.embed-english-v3:0` |
| Embed Multilingual v3 | `cohere.embed-multilingual-v3` |
| Embed Multilingual v3 | `cohere.embed-multilingual-v3:0` |
| Rerank v3.5 | `cohere.rerank-v3-5:0` |

</details>

<details>
<summary><h3>AI21 Labs</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Jamba 1.5 Large | `ai21.jamba-1-5-large-v1:0` |
| Jamba 1.5 Mini | `ai21.jamba-1-5-mini-v1:0` |
| Jamba Instruct | `ai21.jamba-instruct-v1:0` |
| Jurassic-2 Ultra | `ai21.j2-ultra-v1` |
| Jurassic-2 Mid | `ai21.j2-mid-v1` |

</details>

<details>
<summary><h3>Stability AI</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| SD3.5 Large | `stability.sd3-5-large-v1:0` |
| SD3 Large | `stability.sd3-large-v1:0` |
| Stable Image Ultra | `stability.stable-image-ultra-v1:0` |
| Stable Image Ultra v1.1 | `stability.stable-image-ultra-v1:1` |
| Stable Image Core | `stability.stable-image-core-v1:0` |
| Stable Image Core v1.1 | `stability.stable-image-core-v1:1` |
| SDXL 1.0 | `stability.stable-diffusion-xl-v1` |
| Creative Upscale | `stability.stable-creative-upscale-v1:0` |
| Conservative Upscale | `stability.stable-conservative-upscale-v1:0` |
| Fast Upscale | `stability.stable-fast-upscale-v1:0` |
| Image Control Sketch | `stability.stable-image-control-sketch-v1:0` |
| Image Control Structure | `stability.stable-image-control-structure-v1:0` |
| Image Inpaint | `stability.stable-image-inpaint-v1:0` |
| Image Erase Object | `stability.stable-image-erase-object-v1:0` |
| Remove Background | `stability.stable-image-remove-background-v1:0` |
| Search Recolor | `stability.stable-image-search-recolor-v1:0` |
| Search Replace | `stability.stable-image-search-replace-v1:0` |
| Style Guide | `stability.stable-image-style-guide-v1:0` |
| Style Transfer | `stability.stable-style-transfer-v1:0` |
| Outpaint | `stability.stable-outpaint-v1:0` |

</details>

<details>
<summary><h3>DeepSeek</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| DeepSeek R1 | `deepseek.r1-v1:0` |
| DeepSeek V3 | `deepseek.v3-v1:0` |

</details>

<details>
<summary><h3>Google</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Gemma 3 27B | `google.gemma-3-27b-it` |
| Gemma 3 12B | `google.gemma-3-12b-it` |
| Gemma 3 4B | `google.gemma-3-4b-it` |

</details>

<details>
<summary><h3>NVIDIA</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Nemotron Nano 12B | `nvidia.nemotron-nano-12b-v2` |
| Nemotron Nano 9B | `nvidia.nemotron-nano-9b-v2` |
| Nemotron Nano 30B | `nvidia.nemotron-nano-3-30b` |

</details>

<details>
<summary><h3>OpenAI</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| GPT OSS 120B | `openai.gpt-oss-120b-1:0` |
| GPT OSS 20B | `openai.gpt-oss-20b-1:0` |
| GPT OSS Safeguard 120B | `openai.gpt-oss-safeguard-120b` |
| GPT OSS Safeguard 20B | `openai.gpt-oss-safeguard-20b` |

</details>

<details>
<summary><h3>Qwen</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Qwen3 Coder 480B | `qwen.qwen3-coder-480b-a35b-v1:0` |
| Qwen3 235B | `qwen.qwen3-235b-a22b-2507-v1:0` |
| Qwen3 VL 235B | `qwen.qwen3-vl-235b-a22b` |
| Qwen3 Next 80B | `qwen.qwen3-next-80b-a3b` |
| Qwen3 Coder 30B | `qwen.qwen3-coder-30b-a3b-v1:0` |
| Qwen3 32B | `qwen.qwen3-32b-v1:0` |

</details>

<details>
<summary><h3>Moonshot AI</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Kimi K2 Thinking | `moonshot.kimi-k2-thinking` |

</details>

<details>
<summary><h3>MiniMax</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| MiniMax M2 | `minimax.minimax-m2` |

</details>

<details>
<summary><h3>TwelveLabs</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Pegasus 1.2 | `twelvelabs.pegasus-1-2-v1:0` |
| Marengo Embed 3.0 | `twelvelabs.marengo-embed-3-0-v1:0` |
| Marengo Embed 2.7 | `twelvelabs.marengo-embed-2-7-v1:0` |

</details>

<details>
<summary><h3>Writer</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Palmyra X5 | `writer.palmyra-x5-v1:0` |
| Palmyra X4 | `writer.palmyra-x4-v1:0` |

</details>

<details>
<summary><h3>Luma AI</h3></summary>

| Display Name | Model ID |
|:-------------|:---------|
| Luma Ray v2 | `luma.ray-v2:0` |

</details>


<!-- BEDROCK_AVAILABILITY_END -->

## Usage

This repository is automatically updated every hour.

## License

MIT License
