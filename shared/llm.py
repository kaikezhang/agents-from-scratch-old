"""
LLM - A simple wrapper around the DeepSeek API (OpenAI-compatible).

This class provides a minimal interface to interact with a chat-completion LLM.
It intentionally has no magic:
- No retries (added in lesson 03)
- No tool calling (added in lesson 05)
- No memory (added in lesson 07)

Just text in, text out.

Configuration (read from environment):
- DEEPSEEK_API_KEY (or OPENAI_API_KEY) — required
- DEEPSEEK_BASE_URL (or OPENAI_BASE_URL) — defaults to https://api.deepseek.com
- LLM_MODEL — defaults to deepseek-chat
"""

import os

from openai import OpenAI

# Load variables from a local .env file (if present) so users don't have to
# `export` keys in every shell. Safe to call even when there is no .env.
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-chat"


class LLM:
    """
    A minimal wrapper for chat-completion LLM inference.

    Talks to any OpenAI-compatible endpoint. Defaults to DeepSeek.
    This class is intentionally simple and grows throughout the lessons.
    """

    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.2,
        max_tokens: int = 512,
        api_key: str | None = None,
        base_url: str | None = None,
    ):
        """
        Initialize the LLM client.

        Args:
            model: Model name (e.g., "deepseek-chat"). Falls back to LLM_MODEL env var.
            temperature: Sampling temperature (0.0 = deterministic, 1.0 = creative)
            max_tokens: Maximum tokens to generate per response
            api_key: API key. Falls back to DEEPSEEK_API_KEY / OPENAI_API_KEY env vars.
            base_url: API base URL. Falls back to DEEPSEEK_BASE_URL / OPENAI_BASE_URL env vars.
        """
        resolved_key = (
            api_key
            or os.environ.get("DEEPSEEK_API_KEY")
            or os.environ.get("OPENAI_API_KEY")
        )
        if not resolved_key:
            raise RuntimeError(
                "No API key found. Set DEEPSEEK_API_KEY (or OPENAI_API_KEY) "
                "in your environment, or pass api_key= explicitly."
            )

        resolved_base_url = (
            base_url
            or os.environ.get("DEEPSEEK_BASE_URL")
            or os.environ.get("OPENAI_BASE_URL")
            or DEFAULT_BASE_URL
        )

        self.client = OpenAI(api_key=resolved_key, base_url=resolved_base_url)
        self.model = model or os.environ.get("LLM_MODEL", DEFAULT_MODEL)
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(
        self,
        prompt: str,
        temperature: float | None = None,
        stop: list[str] | None = None,
    ) -> str:
        """
        Generate text from a prompt.

        Args:
            prompt: The input text prompt (sent as a single user message)
            temperature: Optional temperature override
            stop: Optional list of stop sequences

        Returns:
            Generated text as a string
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature if temperature is not None else self.temperature,
            max_tokens=self.max_tokens,
            stop=stop,
        )
        return (response.choices[0].message.content or "").strip()


# Backwards-compatible alias so older lesson docs / imports keep working.
LocalLLM = LLM
