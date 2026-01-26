# AWS Bedrock Model Availability Tracker

AWS Bedrock 모델의 리전별 가용성을 추적합니다.

## 모델 가용성 현황

<!-- BEDROCK_AVAILABILITY_START -->

![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--1--26-blue)
 ![Regions](https://img.shields.io/badge/Regions-14-green)
 ![Providers](https://img.shields.io/badge/Providers-17-orange)

> **Last updated:** 2026-01-26 13:20:34 UTC

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
| Nova Canvas | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Lite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Micro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Pro | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Nova Reel | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nova Reel (1) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Image | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Titan Embed Text | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text (8k) | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Titan Embed Text v2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Titan Image Generator v2 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-2-lite-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| amazon.nova-2-lite-v1:0:256k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-2-multimodal-embeddings-v1:0 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-2-sonic-v1:0 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-lite-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-lite-v1:0:300k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-micro-v1:0:128k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-micro-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:1000k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:20k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:8k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-premier-v1:0:mm | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-pro-v1:0:24k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-pro-v1:0:300k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.nova-sonic-v1:0 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.rerank-v1:0 | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.titan-embed-g1-text-02 | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.titan-embed-image-v1:0 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| amazon.titan-embed-text-v2:0:8k | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| amazon.titan-tg1-large | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

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
| Claude Instant (100k) | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:18k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:200k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20240620-v1:0:51k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:18k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:200k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-5-sonnet-20241022-v2:0:51k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-7-sonnet-20250219-v1:0 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| anthropic.claude-3-haiku-20240307-v1:0:200k | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| anthropic.claude-3-haiku-20240307-v1:0:48k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:12k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:200k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-opus-20240229-v1:0:28k | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-3-sonnet-20240229-v1:0:200k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| anthropic.claude-3-sonnet-20240229-v1:0:28k | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| anthropic.claude-haiku-4-5-20251001-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| anthropic.claude-opus-4-1-20250805-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-opus-4-20250514-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| anthropic.claude-opus-4-5-20251101-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| anthropic.claude-sonnet-4-20250514-v1:0 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

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
| cohere.embed-v4:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| cohere.rerank-v3-5:0 | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="deepseek">DeepSeek (2 models, 6 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-2 | ap-northeast-1 | ap-south-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| deepseek.r1-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| deepseek.v3-v1:0 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="google">Google (3 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| google.gemma-3-12b-it | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| google.gemma-3-27b-it | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| google.gemma-3-4b-it | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="luma-ai">Luma AI (1 models, 1 regions)</h3></summary>

| Model | us-west-2 |
|:------|:---:|
| luma.ray-v2:0 | ✅ |

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
| meta.llama3-1-70b-instruct-v1:0:128k | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-1-8b-instruct-v1:0:128k | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-11b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-1b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-3b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-2-90b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-3-70b-instruct-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama3-3-70b-instruct-v1:0:128k | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama4-maverick-17b-instruct-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| meta.llama4-scout-17b-instruct-v1:0 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

</details>

<details>
<summary><h3 id="minimax">MiniMax (1 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| minimax.minimax-m2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="mistral-ai">Mistral AI (13 models, 12 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Mistral 7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral Large | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Mistral Large 2 | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mistral Small | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mixtral 8x7B | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ |
| mistral.magistral-small-2509 | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.ministral-3-14b-instruct | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.ministral-3-3b-instruct | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.ministral-3-8b-instruct | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.mistral-large-3-675b-instruct | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.pixtral-large-2502-v1:0 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| mistral.voxtral-mini-3b-2507 | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |
| mistral.voxtral-small-24b-2507 | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="moonshot-ai">Moonshot AI (1 models, 6 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|
| moonshot.kimi-k2-thinking | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="nvidia">NVIDIA (3 models, 8 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| nvidia.nemotron-nano-12b-v2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| nvidia.nemotron-nano-3-30b | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| nvidia.nemotron-nano-9b-v2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="openai">OpenAI (4 models, 9 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| openai.gpt-oss-120b-1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| openai.gpt-oss-20b-1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| openai.gpt-oss-safeguard-120b | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| openai.gpt-oss-safeguard-20b | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="qwen">Qwen (6 models, 9 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| qwen.qwen3-235b-a22b-2507-v1:0 | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ❌ |
| qwen.qwen3-32b-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen.qwen3-coder-30b-a3b-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen.qwen3-coder-480b-a35b-v1:0 | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| qwen.qwen3-next-80b-a3b | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen.qwen3-vl-235b-a22b | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="stability-ai">Stability AI (16 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| Stable Image Core (1) | ❌ | ❌ | ✅ |
| Stable Image Ultra (1) | ❌ | ❌ | ✅ |
| stability.sd3-5-large-v1:0 | ❌ | ❌ | ✅ |
| stability.stable-conservative-upscale-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-creative-upscale-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-fast-upscale-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-control-sketch-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-control-structure-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-erase-object-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-inpaint-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-remove-background-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-search-recolor-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-search-replace-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-image-style-guide-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-outpaint-v1:0 | ✅ | ✅ | ✅ |
| stability.stable-style-transfer-v1:0 | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="twelvelabs">TwelveLabs (3 models, 14 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|:------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| twelvelabs.marengo-embed-2-7-v1:0 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| twelvelabs.marengo-embed-3-0-v1:0 | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| twelvelabs.pegasus-1-2-v1:0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

</details>

<details>
<summary><h3 id="writer">Writer (2 models, 3 regions)</h3></summary>

| Model | us-east-1 | us-east-2 | us-west-2 |
|:------|:---:|:---:|:---:|
| writer.palmyra-x4-v1:0 | ✅ | ✅ | ✅ |
| writer.palmyra-x5-v1:0 | ✅ | ✅ | ✅ |

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
