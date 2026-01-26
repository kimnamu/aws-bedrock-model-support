/**
 * Model Names - Model ID to human-readable name mapping
 * This file is auto-generated or manually maintained to match src/models/model_names.py
 */

const MODEL_NAME_MAP = {
    // Anthropic Claude
    "anthropic.claude-3-5-sonnet-20241022-v2:0": "Claude 3.5 Sonnet v2",
    "anthropic.claude-3-5-sonnet-20240620-v1:0": "Claude 3.5 Sonnet",
    "anthropic.claude-3-5-haiku-20241022-v1:0": "Claude 3.5 Haiku",
    "anthropic.claude-3-opus-20240229-v1:0": "Claude 3 Opus",
    "anthropic.claude-3-sonnet-20240229-v1:0": "Claude 3 Sonnet",
    "anthropic.claude-3-haiku-20240307-v1:0": "Claude 3 Haiku",
    "anthropic.claude-v2:1": "Claude 2.1",
    "anthropic.claude-v2": "Claude 2",
    "anthropic.claude-instant-v1": "Claude Instant",

    // Amazon Titan
    "amazon.titan-text-premier-v1:0": "Titan Text Premier",
    "amazon.titan-text-express-v1": "Titan Text Express",
    "amazon.titan-text-lite-v1": "Titan Text Lite",
    "amazon.titan-embed-text-v2:0": "Titan Embed Text v2",
    "amazon.titan-embed-text-v1": "Titan Embed Text",
    "amazon.titan-embed-image-v1": "Titan Embed Image",
    "amazon.titan-image-generator-v2:0": "Titan Image Generator v2",
    "amazon.titan-image-generator-v1": "Titan Image Generator",

    // Amazon Nova
    "amazon.nova-pro-v1:0": "Nova Pro",
    "amazon.nova-lite-v1:0": "Nova Lite",
    "amazon.nova-micro-v1:0": "Nova Micro",
    "amazon.nova-canvas-v1:0": "Nova Canvas",
    "amazon.nova-reel-v1:0": "Nova Reel",

    // Meta Llama
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

    // Mistral
    "mistral.mistral-large-2407-v1:0": "Mistral Large 2",
    "mistral.mistral-large-2402-v1:0": "Mistral Large",
    "mistral.mistral-small-2402-v1:0": "Mistral Small",
    "mistral.mixtral-8x7b-instruct-v0:1": "Mixtral 8x7B",
    "mistral.mistral-7b-instruct-v0:2": "Mistral 7B",

    // Cohere
    "cohere.command-r-plus-v1:0": "Command R+",
    "cohere.command-r-v1:0": "Command R",
    "cohere.command-text-v14": "Command",
    "cohere.command-light-text-v14": "Command Light",
    "cohere.embed-english-v3": "Embed English v3",
    "cohere.embed-multilingual-v3": "Embed Multilingual v3",

    // AI21 Labs
    "ai21.jamba-1-5-large-v1:0": "Jamba 1.5 Large",
    "ai21.jamba-1-5-mini-v1:0": "Jamba 1.5 Mini",
    "ai21.jamba-instruct-v1:0": "Jamba Instruct",
    "ai21.j2-ultra-v1": "Jurassic-2 Ultra",
    "ai21.j2-mid-v1": "Jurassic-2 Mid",

    // Stability AI
    "stability.stable-diffusion-xl-v1": "SDXL 1.0",
    "stability.sd3-large-v1:0": "SD3 Large",
    "stability.stable-image-ultra-v1:0": "Stable Image Ultra",
    "stability.stable-image-core-v1:0": "Stable Image Core"
};

/**
 * Get display name for a model ID
 * @param {string} modelId - The AWS Bedrock model ID
 * @returns {string} - Human-readable name or the original model ID if no mapping exists
 */
function getDisplayName(modelId) {
    // Exact match
    if (MODEL_NAME_MAP[modelId]) {
        return MODEL_NAME_MAP[modelId];
    }

    // Try stripping throughput suffix (e.g., :0:28k -> :0)
    const baseId = stripSuffixes(modelId);
    if (MODEL_NAME_MAP[baseId]) {
        const suffix = getSuffixLabel(modelId);
        return MODEL_NAME_MAP[baseId] + suffix;
    }

    // Return original model ID if no mapping found
    return modelId;
}

/**
 * Strip version and throughput suffixes from model ID
 * @param {string} modelId
 * @returns {string}
 */
function stripSuffixes(modelId) {
    // Remove throughput suffix like :0:28k, :0:200k
    let result = modelId.replace(/:\d+:\d+k?$/, '');

    // If no change, normalize version suffix to :0
    if (result === modelId) {
        result = modelId.replace(/:\d+$/, ':0');
    }

    return result;
}

/**
 * Get throughput suffix label
 * @param {string} modelId
 * @returns {string}
 */
function getSuffixLabel(modelId) {
    const match = modelId.match(/:(\d+k?)$/);
    if (match && match[1] !== '0') {
        return ` (${match[1]})`;
    }
    return '';
}
