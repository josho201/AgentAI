# OpenAI GPT-OSS Family of Models: Comprehensive Report

## Introduction
OpenAI has released its first open-source large language model family under an Apache 2.0 license, named **GPT-OSS** (as detailed in [Hugging Face's blog](https://huggingface.co/blog/welcome-openai-gpt-oss) and [Northflank's guide](https://northflank.com/blog/self-host-openai-gpt-oss-120b-open-source-chatgpt)). This marks a significant shift from OpenAI's previous closed-source models (e.g., GPT-3.5, GPT-4), which were only available via API.

## Key Models
GPT-OSS includes two variants:
- **gpt-oss-20b**: 21B parameters (~3.6B active per token), optimized for speed and on-device deployment.
- **gpt-oss-120b**: 117B parameters (~5.1B active), designed for high-performance tasks requiring more compute.

Both models use a **Mixture-of-Experts (MoE)** architecture with 4-bit quantization to optimize memory usage.

## Technical Specifications
| Feature               | gpt-oss-20b       | gpt-oss-120b      |
|-----------------------|--------------------|--------------------|
| Total Parameters      | 21B                | 117B               |
| Active Parameters     | ~3.6B              | ~5.1B              |
| Quantization          | MXFP4 (4-bit)      | MXFP4 (4-bit)      |
| Inference Hardware    | Single H100        | 2×H100 or multi-GPU|
| VRAM Required         | ~16GB              | ~80GB              |

## Licensing and Usage Policy
GPT-OSS is released under the **Apache 2.0 license**, with a minimal usage policy emphasizing safe, responsible deployment:

> "We aim for our tools to be used safely, responsibly, and democratically, while maximizing your control over how you use them."

This aligns with OpenAI's broader commitment to open-source initiatives.

## Deployment Options
- **Local Deployment**: Using frameworks like `vLLM`, `llama.cpp`, or `Ollama`.
- **Cloud Platforms**: Northflank (one-click deployment), Hugging Face Inference Providers, Vast.ai.
- **API Integration**: Compatible with OpenAI's Responses API and other inference services.

## Performance Benchmarks
According to the Northflank article, GPT-OSS-120B achieves performance comparable to OpenAI's `o4-mini` on standard benchmarks (as noted in the [Hugging Face post](https://huggingface.co/blog/welcome-openai-gpt-oss)).

## Conclusion
GPT-OSS represents a pivotal step in OpenAI’s transition toward open-source models, providing developers with high-performance tools for both local and cloud deployments. The release addresses long-standing needs for accessible, customizable AI models while maintaining OpenAI's commitment to safety and ethical use.