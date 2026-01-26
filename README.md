# AWS Bedrock Model Availability Tracker

AWS Bedrock 모델의 리전별 가용성을 추적합니다.

## 모델 가용성 현황

<!-- BEDROCK_AVAILABILITY_START -->

### Summary

- **Total unique models**: 147
- **Total regions**: 14
- **Providers**: 17

  - AI21 Labs: 2 models in 1 regions
  - Amazon: 32 models in 14 regions
  - Anthropic: 31 models in 14 regions
  - Cohere: 8 models in 14 regions
  - DeepSeek: 2 models in 6 regions
  - Google: 3 models in 8 regions
  - Luma AI: 1 models in 1 regions
  - Meta: 19 models in 9 regions
  - MiniMax: 1 models in 8 regions
  - Mistral AI: 13 models in 12 regions
  - Moonshot AI: 1 models in 6 regions
  - NVIDIA: 3 models in 8 regions
  - OpenAI: 4 models in 9 regions
  - Qwen: 6 models in 9 regions
  - Stability AI: 16 models in 3 regions
  - TwelveLabs: 3 models in 14 regions
  - Writer: 2 models in 3 regions

### Table of Contents

- [AI21 Labs](#ai21-labs) (2 models, 1 regions)
- [Amazon](#amazon) (32 models, 14 regions)
- [Anthropic](#anthropic) (31 models, 14 regions)
- [Cohere](#cohere) (8 models, 14 regions)
- [DeepSeek](#deepseek) (2 models, 6 regions)
- [Google](#google) (3 models, 8 regions)
- [Luma AI](#luma-ai) (1 models, 1 regions)
- [Meta](#meta) (19 models, 9 regions)
- [MiniMax](#minimax) (1 models, 8 regions)
- [Mistral AI](#mistral-ai) (13 models, 12 regions)
- [Moonshot AI](#moonshot-ai) (1 models, 6 regions)
- [NVIDIA](#nvidia) (3 models, 8 regions)
- [OpenAI](#openai) (4 models, 9 regions)
- [Qwen](#qwen) (6 models, 9 regions)
- [Stability AI](#stability-ai) (16 models, 3 regions)
- [TwelveLabs](#twelvelabs) (3 models, 14 regions)
- [Writer](#writer) (2 models, 3 regions)

---

### <a id="ai21-labs"></a>AI21 Labs

**2 models** across **1 regions**

| Model | us-east-1 |
|-------|:---:|
| `ai21.jamba-1-5-large-v1:0` | ✅ |
| `ai21.jamba-1-5-mini-v1:0` | ✅ |

### <a id="amazon"></a>Amazon

**32 models** across **14 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `amazon.nova-2-lite-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `amazon.nova-2-lite-v1:0:256k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-2-multimodal-embeddings-v1:0` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-2-sonic-v1:0` | ✅ | - | ✅ | - | - | - | - | - | ✅ | - | - | - | - | - |
| `amazon.nova-canvas-v1:0` | ✅ | - | - | - | - | ✅ | - | - | ✅ | - | - | - | - | - |
| `amazon.nova-lite-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `amazon.nova-lite-v1:0:24k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-lite-v1:0:300k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-micro-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `amazon.nova-micro-v1:0:128k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-micro-v1:0:24k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-premier-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-premier-v1:0:1000k` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-premier-v1:0:20k` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-premier-v1:0:8k` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-premier-v1:0:mm` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-pro-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `amazon.nova-pro-v1:0:24k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-pro-v1:0:300k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-reel-v1:0` | ✅ | - | - | - | - | ✅ | - | - | ✅ | - | - | - | - | - |
| `amazon.nova-reel-v1:1` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.nova-sonic-v1:0` | ✅ | - | - | - | - | - | - | - | ✅ | - | - | - | - | - |
| `amazon.rerank-v1:0` | - | - | ✅ | ✅ | ✅ | - | - | - | ✅ | - | - | - | - | - |
| `amazon.titan-embed-g1-text-02` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.titan-embed-image-v1` | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | - | - | ✅ | ✅ | ✅ |
| `amazon.titan-embed-image-v1:0` | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | - | - | ✅ | ✅ | ✅ |
| `amazon.titan-embed-text-v1` | ✅ | - | ✅ | - | ✅ | - | - | - | ✅ | - | - | - | - | - |
| `amazon.titan-embed-text-v1:2:8k` | ✅ | - | ✅ | - | ✅ | - | - | - | ✅ | - | - | - | - | - |
| `amazon.titan-embed-text-v2:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ |
| `amazon.titan-embed-text-v2:0:8k` | ✅ | - | - | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.titan-image-generator-v2:0` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `amazon.titan-tg1-large` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |

### <a id="anthropic"></a>Anthropic

**31 models** across **14 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `anthropic.claude-3-5-haiku-20241022-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20240620-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `anthropic.claude-3-5-sonnet-20240620-v1:0:18k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20240620-v1:0:200k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20240620-v1:0:51k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20241022-v2:0` | ✅ | ✅ | ✅ | - | - | - | - | - | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `anthropic.claude-3-5-sonnet-20241022-v2:0:18k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20241022-v2:0:200k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-5-sonnet-20241022-v2:0:51k` | - | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-7-sonnet-20250219-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `anthropic.claude-3-haiku-20240307-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `anthropic.claude-3-haiku-20240307-v1:0:200k` | ✅ | ✅ | ✅ | - | - | - | - | ✅ | - | ✅ | - | ✅ | - | - |
| `anthropic.claude-3-haiku-20240307-v1:0:48k` | ✅ | - | ✅ | - | - | ✅ | - | ✅ | - | - | - | ✅ | ✅ | - |
| `anthropic.claude-3-opus-20240229-v1:0` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-opus-20240229-v1:0:12k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-opus-20240229-v1:0:200k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-opus-20240229-v1:0:28k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-3-sonnet-20240229-v1:0` | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `anthropic.claude-3-sonnet-20240229-v1:0:200k` | ✅ | - | ✅ | - | - | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | - | - |
| `anthropic.claude-3-sonnet-20240229-v1:0:28k` | ✅ | - | ✅ | - | - | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `anthropic.claude-haiku-4-5-20251001-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `anthropic.claude-instant-v1:2:100k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-opus-4-1-20250805-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-opus-4-20250514-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-opus-4-5-20251101-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `anthropic.claude-sonnet-4-20250514-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - |
| `anthropic.claude-sonnet-4-5-20250929-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `anthropic.claude-v2:0:100k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-v2:0:18k` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-v2:1:18k` | ✅ | - | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - |
| `anthropic.claude-v2:1:200k` | ✅ | - | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - |

### <a id="cohere"></a>Cohere

**8 models** across **14 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `cohere.command-r-plus-v1:0` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `cohere.command-r-v1:0` | ✅ | - | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `cohere.embed-english-v3` | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ |
| `cohere.embed-english-v3:0:512` | ✅ | - | ✅ | ✅ | - | - | ✅ | ✅ | - | - | - | - | - | ✅ |
| `cohere.embed-multilingual-v3` | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ |
| `cohere.embed-multilingual-v3:0:512` | ✅ | - | ✅ | ✅ | - | - | ✅ | ✅ | - | - | - | - | - | ✅ |
| `cohere.embed-v4:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `cohere.rerank-v3-5:0` | ✅ | - | ✅ | ✅ | ✅ | - | - | - | ✅ | - | - | - | - | - |

### <a id="deepseek"></a>DeepSeek

**2 models** across **6 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-2 | ap-northeast-1 | ap-south-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| `deepseek.r1-v1:0` | ✅ | ✅ | ✅ | - | - | - |
| `deepseek.v3-v1:0` | - | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="google"></a>Google

**3 models** across **8 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `google.gemma-3-12b-it` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `google.gemma-3-27b-it` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `google.gemma-3-4b-it` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="luma-ai"></a>Luma AI

**1 models** across **1 regions**

| Model | us-west-2 |
|-------|:---:|
| `luma.ray-v2:0` | ✅ |

### <a id="meta"></a>Meta

**19 models** across **9 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-south-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `meta.llama3-1-405b-instruct-v1:0` | - | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-1-70b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-1-70b-instruct-v1:0:128k` | - | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-1-8b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-1-8b-instruct-v1:0:128k` | - | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-11b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-11b-instruct-v1:0:128k` | - | - | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-1b-instruct-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | ✅ | - |
| `meta.llama3-2-1b-instruct-v1:0:128k` | - | - | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-3b-instruct-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | ✅ | - |
| `meta.llama3-2-3b-instruct-v1:0:128k` | - | - | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-90b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-2-90b-instruct-v1:0:128k` | - | - | ✅ | - | - | - | - | - | - |
| `meta.llama3-3-70b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama3-3-70b-instruct-v1:0:128k` | - | - | ✅ | - | - | - | - | - | - |
| `meta.llama3-70b-instruct-v1:0` | ✅ | - | ✅ | ✅ | - | - | ✅ | - | ✅ |
| `meta.llama3-8b-instruct-v1:0` | ✅ | - | ✅ | ✅ | - | - | ✅ | - | ✅ |
| `meta.llama4-maverick-17b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |
| `meta.llama4-scout-17b-instruct-v1:0` | ✅ | ✅ | ✅ | - | - | - | - | - | - |

### <a id="minimax"></a>MiniMax

**1 models** across **8 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `minimax.minimax-m2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="mistral-ai"></a>Mistral AI

**13 models** across **12 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `mistral.magistral-small-2509` | ✅ | ✅ | ✅ | - | - | - | - | - | ✅ | - | ✅ | ✅ |
| `mistral.ministral-3-14b-instruct` | ✅ | ✅ | ✅ | - | - | ✅ | ✅ | - | ✅ | - | ✅ | ✅ |
| `mistral.ministral-3-3b-instruct` | ✅ | ✅ | ✅ | - | - | - | - | - | ✅ | - | ✅ | ✅ |
| `mistral.ministral-3-8b-instruct` | ✅ | ✅ | ✅ | - | - | ✅ | ✅ | - | ✅ | - | ✅ | ✅ |
| `mistral.mistral-7b-instruct-v0:2` | ✅ | - | ✅ | ✅ | - | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ |
| `mistral.mistral-large-2402-v1:0` | ✅ | - | ✅ | ✅ | - | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ |
| `mistral.mistral-large-2407-v1:0` | - | - | ✅ | - | - | - | - | - | - | - | - | - |
| `mistral.mistral-large-3-675b-instruct` | ✅ | ✅ | ✅ | - | - | - | - | - | ✅ | - | ✅ | ✅ |
| `mistral.mistral-small-2402-v1:0` | ✅ | - | - | - | - | - | - | - | - | - | - | - |
| `mistral.mixtral-8x7b-instruct-v0:1` | ✅ | - | ✅ | ✅ | - | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ |
| `mistral.pixtral-large-2502-v1:0` | ✅ | ✅ | ✅ | - | ✅ | ✅ | - | ✅ | - | - | - | - |
| `mistral.voxtral-mini-3b-2507` | ✅ | ✅ | ✅ | - | - | ✅ | ✅ | - | ✅ | - | ✅ | ✅ |
| `mistral.voxtral-small-24b-2507` | ✅ | ✅ | ✅ | - | - | ✅ | ✅ | - | ✅ | - | ✅ | ✅ |

### <a id="moonshot-ai"></a>Moonshot AI

**1 models** across **6 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| `moonshot.kimi-k2-thinking` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="nvidia"></a>NVIDIA

**3 models** across **8 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `nvidia.nemotron-nano-12b-v2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `nvidia.nemotron-nano-3-30b` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ |
| `nvidia.nemotron-nano-9b-v2` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="openai"></a>OpenAI

**4 models** across **9 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `openai.gpt-oss-120b-1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `openai.gpt-oss-20b-1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `openai.gpt-oss-safeguard-120b` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ |
| `openai.gpt-oss-safeguard-20b` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="qwen"></a>Qwen

**6 models** across **9 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | eu-central-1 | eu-west-1 | eu-west-2 | ap-northeast-1 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `qwen.qwen3-235b-a22b-2507-v1:0` | - | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | - |
| `qwen.qwen3-32b-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `qwen.qwen3-coder-30b-a3b-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `qwen.qwen3-coder-480b-a35b-v1:0` | - | ✅ | ✅ | - | - | ✅ | ✅ | ✅ | - |
| `qwen.qwen3-next-80b-a3b` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ |
| `qwen.qwen3-vl-235b-a22b` | ✅ | ✅ | ✅ | - | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="stability-ai"></a>Stability AI

**16 models** across **3 regions**

| Model | us-east-1 | us-east-2 | us-west-2 |
|-------|:---:|:---:|:---:|
| `stability.sd3-5-large-v1:0` | - | - | ✅ |
| `stability.stable-conservative-upscale-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-creative-upscale-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-fast-upscale-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-control-sketch-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-control-structure-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-core-v1:1` | - | - | ✅ |
| `stability.stable-image-erase-object-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-inpaint-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-remove-background-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-search-recolor-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-search-replace-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-style-guide-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-image-ultra-v1:1` | - | - | ✅ |
| `stability.stable-outpaint-v1:0` | ✅ | ✅ | ✅ |
| `stability.stable-style-transfer-v1:0` | ✅ | ✅ | ✅ |

### <a id="twelvelabs"></a>TwelveLabs

**3 models** across **14 regions**

| Model | us-east-1 | us-east-2 | us-west-2 | ca-central-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | ap-northeast-1 | ap-northeast-2 | ap-southeast-1 | ap-southeast-2 | ap-south-1 | sa-east-1 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `twelvelabs.marengo-embed-2-7-v1:0` | ✅ | - | - | - | - | ✅ | - | - | - | ✅ | - | - | - | - |
| `twelvelabs.marengo-embed-3-0-v1:0` | ✅ | - | - | - | - | ✅ | - | - | - | ✅ | - | - | - | - |
| `twelvelabs.pegasus-1-2-v1:0` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### <a id="writer"></a>Writer

**2 models** across **3 regions**

| Model | us-east-1 | us-east-2 | us-west-2 |
|-------|:---:|:---:|:---:|
| `writer.palmyra-x4-v1:0` | ✅ | ✅ | ✅ |
| `writer.palmyra-x5-v1:0` | ✅ | ✅ | ✅ |

---

*Last updated: 2026-01-26 12:52:11 UTC*

<!-- BEDROCK_AVAILABILITY_END -->

## 사용법

이 저장소는 매일 자동으로 업데이트됩니다.

## 라이센스

MIT License
