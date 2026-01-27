"""Model Names - Model ID to human-readable name mapping

이 모듈은 AWS Bedrock 모델 ID를 사람이 읽기 쉬운 이름으로 변환합니다.

모델명 매핑 로직:
1. 정확한 매핑이 있으면 사용 (MODEL_NAME_MAP)
2. base ID (throughput suffix 제거)로 매핑 후 suffix 추가
3. Provider별 naming rule에 따라 자동 생성
"""

import re
from typing import Dict, Optional, Tuple


# Model ID → Display name mapping (기본 모델만 정의, throughput variant는 자동 처리)
MODEL_NAME_MAP: Dict[str, str] = {
    # Anthropic Claude - Claude 4 Series
    "anthropic.claude-opus-4-5-20251101-v1:0": "Claude Opus 4.5",
    "anthropic.claude-opus-4-1-20250805-v1:0": "Claude Opus 4.1",
    "anthropic.claude-opus-4-20250514-v1:0": "Claude Opus 4",
    "anthropic.claude-sonnet-4-5-20250929-v1:0": "Claude Sonnet 4.5",
    "anthropic.claude-sonnet-4-20250514-v1:0": "Claude Sonnet 4",
    "anthropic.claude-haiku-4-5-20251001-v1:0": "Claude Haiku 4.5",
    # Anthropic Claude - Claude 3.x Series
    "anthropic.claude-3-7-sonnet-20250219-v1:0": "Claude 3.7 Sonnet",
    "anthropic.claude-3-5-sonnet-20241022-v2:0": "Claude 3.5 Sonnet v2",
    "anthropic.claude-3-5-sonnet-20240620-v1:0": "Claude 3.5 Sonnet",
    "anthropic.claude-3-5-haiku-20241022-v1:0": "Claude 3.5 Haiku",
    "anthropic.claude-3-opus-20240229-v1:0": "Claude 3 Opus",
    "anthropic.claude-3-sonnet-20240229-v1:0": "Claude 3 Sonnet",
    "anthropic.claude-3-haiku-20240307-v1:0": "Claude 3 Haiku",
    # Anthropic Claude - Legacy
    "anthropic.claude-v2:1": "Claude 2.1",
    "anthropic.claude-v2:0": "Claude 2",
    "anthropic.claude-v2": "Claude 2",
    "anthropic.claude-instant-v1": "Claude Instant",
    "anthropic.claude-instant-v1:2": "Claude Instant",

    # Amazon Titan
    "amazon.titan-tg1-large": "Titan Text G1 Large",
    "amazon.titan-text-premier-v1:0": "Titan Text Premier",
    "amazon.titan-text-express-v1": "Titan Text Express",
    "amazon.titan-text-lite-v1": "Titan Text Lite",
    "amazon.titan-embed-text-v2:0": "Titan Embed Text v2",
    "amazon.titan-embed-text-v1": "Titan Embed Text",
    "amazon.titan-embed-text-v1:2": "Titan Embed Text",
    "amazon.titan-embed-g1-text-02": "Titan Embed G1 Text",
    "amazon.titan-embed-image-v1": "Titan Embed Image",
    "amazon.titan-embed-image-v1:0": "Titan Embed Image",
    "amazon.titan-image-generator-v2:0": "Titan Image Generator v2",
    "amazon.titan-image-generator-v1": "Titan Image Generator",

    # Amazon Nova
    "amazon.nova-premier-v1:0": "Nova Premier",
    "amazon.nova-pro-v1:0": "Nova Pro",
    "amazon.nova-lite-v1:0": "Nova Lite",
    "amazon.nova-micro-v1:0": "Nova Micro",
    "amazon.nova-canvas-v1:0": "Nova Canvas",
    "amazon.nova-reel-v1:0": "Nova Reel",
    "amazon.nova-reel-v1:1": "Nova Reel v1.1",
    "amazon.nova-sonic-v1:0": "Nova Sonic",
    "amazon.nova-2-lite-v1:0": "Nova 2 Lite",
    "amazon.nova-2-sonic-v1:0": "Nova 2 Sonic",
    "amazon.nova-2-multimodal-embeddings-v1:0": "Nova 2 Multimodal Embed",
    "amazon.rerank-v1:0": "Amazon Rerank",

    # Meta Llama - Llama 4
    "meta.llama4-scout-17b-instruct-v1:0": "Llama 4 Scout 17B",
    "meta.llama4-maverick-17b-instruct-v1:0": "Llama 4 Maverick 17B",
    # Meta Llama - Llama 3.x
    "meta.llama3-3-70b-instruct-v1:0": "Llama 3.3 70B",
    "meta.llama3-2-90b-instruct-v1:0": "Llama 3.2 90B",
    "meta.llama3-2-11b-instruct-v1:0": "Llama 3.2 11B",
    "meta.llama3-2-3b-instruct-v1:0": "Llama 3.2 3B",
    "meta.llama3-2-1b-instruct-v1:0": "Llama 3.2 1B",
    "meta.llama3-1-405b-instruct-v1:0": "Llama 3.1 405B",
    "meta.llama3-1-70b-instruct-v1:0": "Llama 3.1 70B",
    "meta.llama3-1-8b-instruct-v1:0": "Llama 3.1 8B",
    "meta.llama3-70b-instruct-v1:0": "Llama 3 70B",
    "meta.llama3-8b-instruct-v1:0": "Llama 3 8B",
    "meta.llama2-70b-chat-v1": "Llama 2 70B",
    "meta.llama2-13b-chat-v1": "Llama 2 13B",

    # Mistral AI
    "mistral.mistral-large-3-675b-instruct": "Mistral Large 3 675B",
    "mistral.mistral-large-2407-v1:0": "Mistral Large 2",
    "mistral.mistral-large-2402-v1:0": "Mistral Large",
    "mistral.mistral-small-2402-v1:0": "Mistral Small",
    "mistral.mixtral-8x7b-instruct-v0:1": "Mixtral 8x7B",
    "mistral.mistral-7b-instruct-v0:2": "Mistral 7B",
    "mistral.magistral-small-2509": "Magistral Small",
    "mistral.ministral-3-14b-instruct": "Ministral 14B",
    "mistral.ministral-3-8b-instruct": "Ministral 8B",
    "mistral.ministral-3-3b-instruct": "Ministral 3B",
    "mistral.pixtral-large-2502-v1:0": "Pixtral Large",
    "mistral.voxtral-small-24b-2507": "Voxtral Small 24B",
    "mistral.voxtral-mini-3b-2507": "Voxtral Mini 3B",

    # Cohere
    "cohere.command-r-plus-v1:0": "Command R+",
    "cohere.command-r-v1:0": "Command R",
    "cohere.command-text-v14": "Command",
    "cohere.command-light-text-v14": "Command Light",
    "cohere.embed-v4:0": "Embed v4",
    "cohere.embed-english-v3": "Embed English v3",
    "cohere.embed-english-v3:0": "Embed English v3",
    "cohere.embed-multilingual-v3": "Embed Multilingual v3",
    "cohere.embed-multilingual-v3:0": "Embed Multilingual v3",
    "cohere.rerank-v3-5:0": "Rerank v3.5",

    # AI21 Labs
    "ai21.jamba-1-5-large-v1:0": "Jamba 1.5 Large",
    "ai21.jamba-1-5-mini-v1:0": "Jamba 1.5 Mini",
    "ai21.jamba-instruct-v1:0": "Jamba Instruct",
    "ai21.j2-ultra-v1": "Jurassic-2 Ultra",
    "ai21.j2-mid-v1": "Jurassic-2 Mid",

    # Stability AI
    "stability.stable-diffusion-xl-v1": "SDXL 1.0",
    "stability.sd3-large-v1:0": "SD3 Large",
    "stability.sd3-5-large-v1:0": "SD3.5 Large",
    "stability.stable-image-ultra-v1:0": "Stable Image Ultra",
    "stability.stable-image-ultra-v1:1": "Stable Image Ultra v1.1",
    "stability.stable-image-core-v1:0": "Stable Image Core",
    "stability.stable-image-core-v1:1": "Stable Image Core v1.1",
    "stability.stable-creative-upscale-v1:0": "Creative Upscale",
    "stability.stable-conservative-upscale-v1:0": "Conservative Upscale",
    "stability.stable-fast-upscale-v1:0": "Fast Upscale",
    "stability.stable-image-control-sketch-v1:0": "Image Control Sketch",
    "stability.stable-image-control-structure-v1:0": "Image Control Structure",
    "stability.stable-image-inpaint-v1:0": "Image Inpaint",
    "stability.stable-image-erase-object-v1:0": "Image Erase Object",
    "stability.stable-image-remove-background-v1:0": "Remove Background",
    "stability.stable-image-search-recolor-v1:0": "Search Recolor",
    "stability.stable-image-search-replace-v1:0": "Search Replace",
    "stability.stable-image-style-guide-v1:0": "Style Guide",
    "stability.stable-style-transfer-v1:0": "Style Transfer",
    "stability.stable-outpaint-v1:0": "Outpaint",

    # DeepSeek
    "deepseek.r1-v1:0": "DeepSeek R1",
    "deepseek.v3-v1:0": "DeepSeek V3",

    # Google
    "google.gemma-3-27b-it": "Gemma 3 27B",
    "google.gemma-3-12b-it": "Gemma 3 12B",
    "google.gemma-3-4b-it": "Gemma 3 4B",

    # NVIDIA
    "nvidia.nemotron-nano-12b-v2": "Nemotron Nano 12B",
    "nvidia.nemotron-nano-9b-v2": "Nemotron Nano 9B",
    "nvidia.nemotron-nano-3-30b": "Nemotron Nano 30B",

    # OpenAI
    "openai.gpt-oss-120b-1:0": "GPT OSS 120B",
    "openai.gpt-oss-20b-1:0": "GPT OSS 20B",
    "openai.gpt-oss-safeguard-120b": "GPT OSS Safeguard 120B",
    "openai.gpt-oss-safeguard-20b": "GPT OSS Safeguard 20B",

    # Qwen
    "qwen.qwen3-235b-a22b-2507-v1:0": "Qwen3 235B",
    "qwen.qwen3-32b-v1:0": "Qwen3 32B",
    "qwen.qwen3-coder-480b-a35b-v1:0": "Qwen3 Coder 480B",
    "qwen.qwen3-coder-30b-a3b-v1:0": "Qwen3 Coder 30B",
    "qwen.qwen3-next-80b-a3b": "Qwen3 Next 80B",
    "qwen.qwen3-vl-235b-a22b": "Qwen3 VL 235B",

    # Moonshot AI
    "moonshot.kimi-k2-thinking": "Kimi K2 Thinking",

    # MiniMax
    "minimax.minimax-m2": "MiniMax M2",

    # TwelveLabs
    "twelvelabs.pegasus-1-2-v1:0": "Pegasus 1.2",
    "twelvelabs.marengo-embed-3-0-v1:0": "Marengo Embed 3.0",
    "twelvelabs.marengo-embed-2-7-v1:0": "Marengo Embed 2.7",

    # Writer
    "writer.palmyra-x5-v1:0": "Palmyra X5",
    "writer.palmyra-x4-v1:0": "Palmyra X4",

    # Luma AI
    "luma.ray-v2:0": "Luma Ray v2",
}


def get_display_name(model_id: str, fallback_to_id: bool = False) -> str:
    """
    Convert model ID to human-readable name.

    Args:
        model_id: AWS Bedrock model ID
        fallback_to_id: If True, return model_id as-is when no mapping exists
                        Default changed to False to always try auto-generation

    Returns:
        str: Display name for the model
    """
    # 1. 정확한 매핑이 있으면 사용
    if model_id in MODEL_NAME_MAP:
        return MODEL_NAME_MAP[model_id]

    # 2. Base ID로 매핑 시도 (throughput suffix 제거)
    base_id, suffix_label = _extract_base_and_suffix(model_id)
    if base_id in MODEL_NAME_MAP:
        return f"{MODEL_NAME_MAP[base_id]}{suffix_label}"

    # 3. Provider별 naming rule에 따라 자동 생성
    auto_name = _auto_generate_name(model_id)
    if auto_name:
        return auto_name

    # 4. Fallback: 원본 ID 반환 또는 generic 파싱
    if fallback_to_id:
        return model_id
    return _generic_parse(model_id)


def _extract_base_and_suffix(model_id: str) -> Tuple[str, str]:
    """
    모델 ID에서 base ID와 suffix label을 추출합니다.

    Examples:
        anthropic.claude-3-5-sonnet-20240620-v1:0:18k → (anthropic.claude-3-5-sonnet-20240620-v1:0, " (18k)")
        amazon.nova-pro-v1:0:24k → (amazon.nova-pro-v1:0, " (24k)")
        meta.llama3-1-70b-instruct-v1:0:128k → (meta.llama3-1-70b-instruct-v1:0, " (128k)")
    """
    # Pattern: :version:throughput (e.g., :0:18k, :0:200k, :0:128k, :0:mm)
    match = re.match(r'^(.+):(\d+):(\d+k|mm)$', model_id)
    if match:
        base = f"{match.group(1)}:{match.group(2)}"
        suffix = match.group(3)
        return base, f" ({suffix})"

    # Pattern: :version (e.g., :0, :1) - normalize to :0 for lookup
    match = re.match(r'^(.+):(\d+)$', model_id)
    if match:
        base_without_version = match.group(1)
        version = match.group(2)
        # Try both the exact version and :0
        return f"{base_without_version}:{version}", ""

    return model_id, ""


def _auto_generate_name(model_id: str) -> Optional[str]:
    """
    Provider별 naming rule에 따라 모델명을 자동 생성합니다.
    """
    if not "." in model_id:
        return None

    provider, model_part = model_id.split(".", 1)

    # Provider별 naming rule 적용
    generators = {
        "anthropic": _generate_anthropic_name,
        "amazon": _generate_amazon_name,
        "meta": _generate_meta_name,
        "mistral": _generate_mistral_name,
        "cohere": _generate_cohere_name,
        "ai21": _generate_ai21_name,
        "stability": _generate_stability_name,
        "deepseek": _generate_deepseek_name,
        "google": _generate_google_name,
        "nvidia": _generate_nvidia_name,
        "openai": _generate_openai_name,
        "qwen": _generate_qwen_name,
        "moonshot": _generate_moonshot_name,
        "minimax": _generate_minimax_name,
        "twelvelabs": _generate_twelvelabs_name,
        "writer": _generate_writer_name,
        "luma": _generate_luma_name,
    }

    generator = generators.get(provider)
    if generator:
        return generator(model_part)

    return None


def _generate_anthropic_name(model_part: str) -> Optional[str]:
    """
    Anthropic Claude 모델명 생성

    Patterns:
    - claude-opus-4-5-20251101-v1:0 → Claude Opus 4.5
    - claude-3-5-sonnet-20240620-v1:0 → Claude 3.5 Sonnet
    - claude-3-5-sonnet-20240620-v1:0:18k → Claude 3.5 Sonnet (18k)
    - claude-v2:0:18k → Claude 2 (18k)
    - claude-instant-v1:2:100k → Claude Instant (100k)
    """
    # Extract throughput suffix
    throughput = ""
    match = re.search(r':(\d+k)$', model_part)
    if match:
        throughput = f" ({match.group(1)})"
        model_part = model_part[:match.start()]

    # Remove version suffix (:0, :1, :2)
    model_part = re.sub(r':\d+$', '', model_part)

    # Claude 4.x series (opus, sonnet, haiku with version)
    # claude-opus-4-5-20251101-v1 → Claude Opus 4.5
    match = re.match(r'claude-(opus|sonnet|haiku)-(\d+)-(\d+)?-?\d*-?v?\d*', model_part)
    if match:
        tier = match.group(1).capitalize()
        major = match.group(2)
        minor = match.group(3)
        if minor:
            return f"Claude {tier} {major}.{minor}{throughput}"
        return f"Claude {tier} {major}{throughput}"

    # Claude 3.x series
    # claude-3-5-sonnet-20240620-v1 → Claude 3.5 Sonnet
    # claude-3-opus-20240229-v1 → Claude 3 Opus
    match = re.match(r'claude-(\d+)-?(\d+)?-(opus|sonnet|haiku)-\d+-v\d+', model_part)
    if match:
        major = match.group(1)
        minor = match.group(2)
        tier = match.group(3).capitalize()
        if minor:
            return f"Claude {major}.{minor} {tier}{throughput}"
        return f"Claude {major} {tier}{throughput}"

    # Legacy Claude
    # claude-v2:1 → Claude 2.1
    # claude-v2:0 → Claude 2
    match = re.match(r'claude-v(\d+)', model_part)
    if match:
        version = match.group(1)
        return f"Claude {version}{throughput}"

    # Claude Instant
    match = re.match(r'claude-instant-v(\d+)', model_part)
    if match:
        return f"Claude Instant{throughput}"

    return None


def _generate_amazon_name(model_part: str) -> Optional[str]:
    """
    Amazon 모델명 생성

    Patterns:
    - nova-pro-v1:0 → Nova Pro
    - nova-2-lite-v1:0:256k → Nova 2 Lite (256k)
    - titan-embed-text-v2:0:8k → Titan Embed Text v2 (8k)
    """
    # Extract throughput suffix
    throughput = ""
    match = re.search(r':(\d+k)$', model_part)
    if match:
        throughput = f" ({match.group(1)})"
        model_part = model_part[:match.start()]

    # Remove version suffix
    model_part = re.sub(r':\d+$', '', model_part)

    # Nova models
    # nova-pro-v1 → Nova Pro
    # nova-2-lite-v1 → Nova 2 Lite
    match = re.match(r'nova-(\d+)?-?([a-z-]+)-v[\d.]+', model_part)
    if match:
        version = match.group(1)
        name_part = match.group(2).replace("-", " ").title()
        if version:
            return f"Nova {version} {name_part}{throughput}"
        return f"Nova {name_part}{throughput}"

    # Titan models
    # titan-embed-text-v2 → Titan Embed Text v2
    match = re.match(r'titan-([a-z-]+)-v([\d.]+)', model_part)
    if match:
        name_part = match.group(1).replace("-", " ").title()
        version = match.group(2)
        return f"Titan {name_part} v{version}{throughput}"

    # titan-tg1-large → Titan Text G1 Large
    match = re.match(r'titan-([a-z]+)(\d+)-([a-z]+)', model_part)
    if match:
        return f"Titan {match.group(1).upper()}{match.group(2)} {match.group(3).capitalize()}{throughput}"

    return None


def _generate_meta_name(model_part: str) -> Optional[str]:
    """
    Meta Llama 모델명 생성

    Patterns:
    - llama3-1-70b-instruct-v1:0 → Llama 3.1 70B
    - llama3-2-11b-instruct-v1:0:128k → Llama 3.2 11B (128k)
    - llama4-scout-17b-instruct-v1:0 → Llama 4 Scout 17B
    """
    # Extract throughput suffix
    throughput = ""
    match = re.search(r':(\d+k)$', model_part)
    if match:
        throughput = f" ({match.group(1)})"
        model_part = model_part[:match.start()]

    # Remove version suffix
    model_part = re.sub(r':\d+$', '', model_part)

    # Llama 4 with variant (scout, maverick)
    match = re.match(r'llama(\d+)-([a-z]+)-(\d+b)-instruct-v\d+', model_part)
    if match:
        version = match.group(1)
        variant = match.group(2).capitalize()
        size = match.group(3).upper()
        return f"Llama {version} {variant} {size}{throughput}"

    # Llama 3.x
    # llama3-1-70b-instruct-v1 → Llama 3.1 70B
    match = re.match(r'llama(\d+)-(\d+)-(\d+b)-instruct-v\d+', model_part)
    if match:
        major = match.group(1)
        minor = match.group(2)
        size = match.group(3).upper()
        return f"Llama {major}.{minor} {size}{throughput}"

    # Llama 3 base
    match = re.match(r'llama(\d+)-(\d+b)-instruct-v\d+', model_part)
    if match:
        version = match.group(1)
        size = match.group(2).upper()
        return f"Llama {version} {size}{throughput}"

    return None


def _generate_mistral_name(model_part: str) -> Optional[str]:
    """
    Mistral AI 모델명 생성

    Patterns:
    - mistral-large-2402-v1:0 → Mistral Large
    - mixtral-8x7b-instruct-v0:1 → Mixtral 8x7B
    - ministral-3-14b-instruct → Ministral 14B
    """
    # Remove version suffixes
    model_part = re.sub(r':\d+$', '', model_part)
    model_part = re.sub(r'-v\d+$', '', model_part)

    # Mistral Large with date
    match = re.match(r'mistral-large-(\d{4})', model_part)
    if match:
        return "Mistral Large"

    # Mixtral
    match = re.match(r'mixtral-(\d+x\d+b)-instruct', model_part)
    if match:
        return f"Mixtral {match.group(1).upper()}"

    # Ministral
    match = re.match(r'ministral-\d+-(\d+b)-instruct', model_part)
    if match:
        return f"Ministral {match.group(1).upper()}"

    # Magistral
    match = re.match(r'magistral-([a-z]+)', model_part)
    if match:
        return f"Magistral {match.group(1).capitalize()}"

    # Voxtral
    match = re.match(r'voxtral-([a-z]+)-(\d+b)', model_part)
    if match:
        return f"Voxtral {match.group(1).capitalize()} {match.group(2).upper()}"

    # Pixtral
    if model_part.startswith("pixtral"):
        return "Pixtral Large"

    return None


def _generate_cohere_name(model_part: str) -> Optional[str]:
    """
    Cohere 모델명 생성

    Patterns:
    - embed-english-v3:0:512 → Embed English v3 (512)
    - command-r-plus-v1:0 → Command R+
    """
    # Extract size suffix (e.g., :512)
    size = ""
    match = re.search(r':(\d+)$', model_part)
    if match:
        size = f" ({match.group(1)})"
        model_part = model_part[:match.start()]

    # Remove version suffix
    model_part = re.sub(r':\d+$', '', model_part)

    # Embed models
    match = re.match(r'embed-([a-z]+)-v(\d+)', model_part)
    if match:
        lang = match.group(1).capitalize()
        version = match.group(2)
        return f"Embed {lang} v{version}{size}"

    # Embed v4
    if model_part.startswith("embed-v"):
        match = re.match(r'embed-v(\d+)', model_part)
        if match:
            return f"Embed v{match.group(1)}{size}"

    # Command models
    if "command-r-plus" in model_part:
        return f"Command R+{size}"
    if "command-r" in model_part:
        return f"Command R{size}"

    # Rerank
    match = re.match(r'rerank-v([\d-]+)', model_part)
    if match:
        return f"Rerank v{match.group(1).replace('-', '.')}{size}"

    return None


def _generate_ai21_name(model_part: str) -> Optional[str]:
    """AI21 Labs 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # Jamba
    match = re.match(r'jamba-(\d+)-(\d+)-(large|mini)', model_part)
    if match:
        return f"Jamba {match.group(1)}.{match.group(2)} {match.group(3).capitalize()}"

    # Jurassic
    match = re.match(r'j(\d+)-(ultra|mid)', model_part)
    if match:
        return f"Jurassic-{match.group(1)} {match.group(2).capitalize()}"

    return None


def _generate_stability_name(model_part: str) -> Optional[str]:
    """Stability AI 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # SD3.5
    if "sd3-5-large" in model_part:
        return "SD3.5 Large"
    if "sd3-large" in model_part:
        return "SD3 Large"

    # Stable Image operations
    ops = {
        "stable-image-ultra": "Stable Image Ultra",
        "stable-image-core": "Stable Image Core",
        "stable-creative-upscale": "Creative Upscale",
        "stable-conservative-upscale": "Conservative Upscale",
        "stable-fast-upscale": "Fast Upscale",
        "stable-image-control-sketch": "Image Control Sketch",
        "stable-image-control-structure": "Image Control Structure",
        "stable-image-inpaint": "Image Inpaint",
        "stable-image-erase-object": "Image Erase Object",
        "stable-image-remove-background": "Remove Background",
        "stable-image-search-recolor": "Search Recolor",
        "stable-image-search-replace": "Search Replace",
        "stable-image-style-guide": "Style Guide",
        "stable-style-transfer": "Style Transfer",
        "stable-outpaint": "Outpaint",
    }

    for key, name in ops.items():
        if key in model_part:
            # Check for version suffix
            match = re.search(r'-v(\d+):(\d+)$', model_part)
            if match and match.group(2) != "0":
                return f"{name} v{match.group(1)}.{match.group(2)}"
            return name

    return None


def _generate_deepseek_name(model_part: str) -> Optional[str]:
    """DeepSeek 모델명 생성"""
    if model_part.startswith("r1"):
        return "DeepSeek R1"
    if model_part.startswith("v3"):
        return "DeepSeek V3"
    return None


def _generate_google_name(model_part: str) -> Optional[str]:
    """Google 모델명 생성"""
    # gemma-3-27b-it → Gemma 3 27B
    match = re.match(r'gemma-(\d+)-(\d+b)', model_part)
    if match:
        return f"Gemma {match.group(1)} {match.group(2).upper()}"
    return None


def _generate_nvidia_name(model_part: str) -> Optional[str]:
    """NVIDIA 모델명 생성"""
    # nemotron-nano-12b-v2 → Nemotron Nano 12B
    match = re.match(r'nemotron-nano-(\d+b)', model_part)
    if match:
        return f"Nemotron Nano {match.group(1).upper()}"

    # nemotron-nano-3-30b → Nemotron Nano 30B
    match = re.match(r'nemotron-nano-\d+-(\d+b)', model_part)
    if match:
        return f"Nemotron Nano {match.group(1).upper()}"

    return None


def _generate_openai_name(model_part: str) -> Optional[str]:
    """OpenAI 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # gpt-oss-safeguard-120b → GPT OSS Safeguard 120B
    match = re.match(r'gpt-oss-safeguard-(\d+b)', model_part)
    if match:
        return f"GPT OSS Safeguard {match.group(1).upper()}"

    # gpt-oss-120b-1 → GPT OSS 120B
    match = re.match(r'gpt-oss-(\d+b)', model_part)
    if match:
        return f"GPT OSS {match.group(1).upper()}"

    return None


def _generate_qwen_name(model_part: str) -> Optional[str]:
    """Qwen 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # qwen3-coder-480b-a35b-v1 → Qwen3 Coder 480B
    match = re.match(r'qwen(\d+)-coder-(\d+b)', model_part)
    if match:
        return f"Qwen{match.group(1)} Coder {match.group(2).upper()}"

    # qwen3-vl-235b-a22b → Qwen3 VL 235B
    match = re.match(r'qwen(\d+)-vl-(\d+b)', model_part)
    if match:
        return f"Qwen{match.group(1)} VL {match.group(2).upper()}"

    # qwen3-next-80b-a3b → Qwen3 Next 80B
    match = re.match(r'qwen(\d+)-next-(\d+b)', model_part)
    if match:
        return f"Qwen{match.group(1)} Next {match.group(2).upper()}"

    # qwen3-235b-a22b-2507-v1 → Qwen3 235B
    match = re.match(r'qwen(\d+)-(\d+b)', model_part)
    if match:
        return f"Qwen{match.group(1)} {match.group(2).upper()}"

    return None


def _generate_moonshot_name(model_part: str) -> Optional[str]:
    """Moonshot AI 모델명 생성"""
    if "kimi-k2-thinking" in model_part:
        return "Kimi K2 Thinking"
    return None


def _generate_minimax_name(model_part: str) -> Optional[str]:
    """MiniMax 모델명 생성"""
    if "minimax-m2" in model_part:
        return "MiniMax M2"
    return None


def _generate_twelvelabs_name(model_part: str) -> Optional[str]:
    """TwelveLabs 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # pegasus-1-2-v1 → Pegasus 1.2
    match = re.match(r'pegasus-(\d+)-(\d+)', model_part)
    if match:
        return f"Pegasus {match.group(1)}.{match.group(2)}"

    # marengo-embed-3-0-v1 → Marengo Embed 3.0
    match = re.match(r'marengo-embed-(\d+)-(\d+)', model_part)
    if match:
        return f"Marengo Embed {match.group(1)}.{match.group(2)}"

    return None


def _generate_writer_name(model_part: str) -> Optional[str]:
    """Writer 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # palmyra-x5-v1 → Palmyra X5
    match = re.match(r'palmyra-x(\d+)', model_part)
    if match:
        return f"Palmyra X{match.group(1)}"

    return None


def _generate_luma_name(model_part: str) -> Optional[str]:
    """Luma AI 모델명 생성"""
    model_part = re.sub(r':\d+$', '', model_part)

    # ray-v2 → Luma Ray v2
    match = re.match(r'ray-v(\d+)', model_part)
    if match:
        return f"Luma Ray v{match.group(1)}"

    return None


def _generic_parse(model_id: str) -> str:
    """
    Generic fallback parser for unknown model IDs.
    """
    # Extract model-name from provider.model-name format
    if "." in model_id:
        model_part = model_id.split(".", 1)[1]
    else:
        model_part = model_id

    # Remove version/date/throughput suffixes
    model_part = re.sub(r'-\d{8}-v\d+', '', model_part)  # -20240620-v1
    model_part = re.sub(r'-v\d+', '', model_part)  # -v1
    model_part = re.sub(r':\d+:\d+k?$', '', model_part)  # :0:28k
    model_part = re.sub(r':\d+$', '', model_part)  # :0

    # Replace hyphens with spaces
    words = model_part.replace("-", " ").split()

    result_words = []
    i = 0
    while i < len(words):
        word = words[i]

        # Handle version numbers (e.g., 3 5 → 3.5)
        if word.isdigit() and i + 1 < len(words) and words[i + 1].isdigit():
            result_words.append(f"{word}.{words[i + 1]}")
            i += 2
            continue

        # Model size (e.g., 70b, 8b)
        if re.match(r'^\d+[bB]$', word):
            result_words.append(word.upper())
        else:
            result_words.append(word.capitalize())

        i += 1

    return " ".join(result_words)
