# AWS Bedrock Model Availability Tracker

AWS Bedrock 모델의 리전별 가용성을 추적합니다.

## 모델 가용성 현황

<!-- BEDROCK_AVAILABILITY_START -->

![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--1--27-blue)
 ![Regions](https://img.shields.io/badge/Regions-14-green)
 ![Providers](https://img.shields.io/badge/Providers-17-orange)

> **Last updated:** 2026-01-27 00:20:59 UTC

## Table of Contents

- [AI21 Labs](#ai21-labs) - 2 models, 1 regions
- [Amazon](#amazon) - 32 models, 14 regions
- [Anthropic](#anthropic) - 31 models, 14 regions
- [Cohere](#cohere) - 8 models, 14 regions
- [DeepSeek](#deepseek) - 2 models, 6 regions
- [Google](#google) - 3 models, 8 regions
- [Luma AI](#luma-ai) - 1 models, 1 regions
- [Meta](#meta) - 19 models, 9 regions
- [MiniMax](#minimax) - 1 models, 8 regions
- [Mistral AI](#mistral-ai) - 13 models, 12 regions
- [Moonshot AI](#moonshot-ai) - 1 models, 6 regions
- [NVIDIA](#nvidia) - 3 models, 8 regions
- [OpenAI](#openai) - 4 models, 9 regions
- [Qwen](#qwen) - 6 models, 9 regions
- [Stability AI](#stability-ai) - 16 models, 3 regions
- [TwelveLabs](#twelvelabs) - 3 models, 14 regions
- [Writer](#writer) - 2 models, 3 regions

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
| Amazon Rerank | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova 2 Lite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova 2 Multimodal Embed | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova 2 Sonic | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Canvas | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Lite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Micro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Premier | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Pro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Reel | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Reel v1.1 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Sonic | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed G1 Text | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Image | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Titan Embed Image | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Titan Embed Text | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text (8k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text v2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Titan Image Generator v2 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Text G1 Large | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-2-lite-v1:0:256k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-lite-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-lite-v1:0:300k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-micro-v1:0:128k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-micro-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:1000k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:20k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:8k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:mm | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-pro-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-pro-v1:0:300k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.titan-embed-text-v2:0:8k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="anthropic">Anthropic (31 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Claude 2 (100k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2 (18k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2 (18k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 2 (200k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Haiku | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude 3 Opus | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3 Sonnet | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude 3.5 Haiku | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude 3.5 Sonnet | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.5 Sonnet v2 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude 3.7 Sonnet | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Haiku 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Instant (100k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Opus 4 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Opus 4.1 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Claude Opus 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Sonnet 4 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Claude Sonnet 4.5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:18k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:200k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:51k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:18k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:200k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:51k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-haiku-20240307-v1:0:200k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| anthropic.claude-3-haiku-20240307-v1:0:48k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:12k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:200k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:28k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-sonnet-20240229-v1:0:200k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| anthropic.claude-3-sonnet-20240229-v1:0:28k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |

</details>

<details>
<summary><h3 id="cohere">Cohere (8 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Command R | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Command R+ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Embed English v3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Embed English v3 (512) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Embed Multilingual v3 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Embed Multilingual v3 (512) | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Embed v4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
| Gemma 3 12B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma 3 27B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
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
| Llama 3 70B | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Llama 3 8B | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Llama 3.1 405B | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 70B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.1 8B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 11B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.2 1B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Llama 3.2 3B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Llama 3.2 90B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 3.3 70B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 4 Maverick 17B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Llama 4 Scout 17B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-1-70b-instruct-v1:0:128k | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-1-8b-instruct-v1:0:128k | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-11b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-1b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-3b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-90b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-3-70b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

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
| Magistral Small | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ministral 14B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ministral 3B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Ministral 8B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Mistral 7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral Large | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral Large 2 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mistral Large 3 675B | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Mistral Small | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mixtral 8x7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Pixtral Large | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Voxtral Mini 3B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| Voxtral Small 24B | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |

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
| Nemotron Nano 30B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Nemotron Nano 9B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

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
| Qwen3 235B | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Qwen3 32B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 Coder 30B | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 Coder 480B | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Qwen3 Next 80B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3 VL 235B | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="stability-ai">Stability AI (16 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| Conservative Upscale | ✅ | ✅ | ✅ |
| Creative Upscale | ✅ | ✅ | ✅ |
| Fast Upscale | ✅ | ✅ | ✅ |
| Image Control Sketch | ✅ | ✅ | ✅ |
| Image Control Structure | ✅ | ✅ | ✅ |
| Image Erase Object | ✅ | ✅ | ✅ |
| Image Inpaint | ✅ | ✅ | ✅ |
| Outpaint | ✅ | ✅ | ✅ |
| Remove Background | ✅ | ✅ | ✅ |
| SD3.5 Large | ❌ | ❌ | ✅ |
| Search Recolor | ✅ | ✅ | ✅ |
| Search Replace | ✅ | ✅ | ✅ |
| Stable Image Core v1.1 | ❌ | ❌ | ✅ |
| Stable Image Ultra v1.1 | ❌ | ❌ | ✅ |
| Style Guide | ✅ | ✅ | ✅ |
| Style Transfer | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="twelvelabs">TwelveLabs (3 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Marengo Embed 2.7 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Marengo Embed 3.0 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Pegasus 1.2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="writer">Writer (2 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| Palmyra X4 | ✅ | ✅ | ✅ |
| Palmyra X5 | ✅ | ✅ | ✅ |

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

## 사용법

이 저장소는 매일 자동으로 업데이트됩니다.

## 라이센스

MIT License
