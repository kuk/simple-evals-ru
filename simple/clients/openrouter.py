
import re
import logging

import aiohttp

from .common import (
    RateLimiter,
    retrying
)


logger = logging.getLogger("simple")


class OpenrouterClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = aiohttp.ClientSession()

        self.rate_limiter = RateLimiter()
        self.request_count = 0
        self.model_pricing = {}

    @retrying
    async def post_request(self, url, data, timeout=None):
        response = await self.session.post(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json=data,
            timeout=aiohttp.ClientTimeout(total=timeout)
        )
        response.raise_for_status()
        return await response.json()

    @retrying
    async def get_request(self, url, timeout=5):
        response = await self.session.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
            },
            timeout=aiohttp.ClientTimeout(total=timeout)
        )
        response.raise_for_status()
        return await response.json()

    async def chat_completions(self, **kwargs):
        return await self.post_request(
            url="https://openrouter.ai/api/v1/chat/completions",
            data=kwargs,
            timeout=120
        )

        # {"id": "gen-1733991024-UnDSgks1KnkCAbFjED5P",
        #  "provider": "OpenAI",
        #  "model": "openai/gpt-4o-mini-2024-07-18",
        #  "object": "chat.completion",
        #  "created": 1733991024,
        #  "choices": [{"logprobs": None,
        #    "finish_reason": "stop",
        #    "index": 0,
        #    "message": {"role": "assistant", "content": "[Б]", "refusal": ""}}],
        #  "system_fingerprint": "fp_bba3c8e70b",
        #  "usage": {"prompt_tokens": 1450,
        #   "completion_tokens": 3,
        #   "total_tokens": 1453}}

    async def auth_key(self):
        response = await self.get_request("https://openrouter.ai/api/v1/auth/key")
        return response["data"]

        # {"label": "sk-or-v1-446...596",
        #  "limit": None,
        #  "usage": 0.926944265,
        #  "limit_remaining": None,
        #  "is_free_tier": False,
        #  "rate_limit": {"requests": 40, "interval": "10s"}}}

    async def models(self):
        response = await self.get_request("https://openrouter.ai/api/v1/models")
        return response["data"]

        # [{"id": "liquid/lfm-7b",
        #   "name": "Liquid: LFM 7B",
        #   "created": 1737806883,
        #   "description": "LFM-7B, a new best-in .. for benchmarks and more info.",
        #   "context_length": 32768,
        #   "architecture": {"modality": "text->text",
        #    "tokenizer": "Other",
        #    "instruct_type": "vicuna"},
        #   "pricing": {"prompt": "0.00000001",
        #    "completion": "0.00000001",
        #    "image": "0",
        #    "request": "0"},
        #   "top_provider": {"context_length": 32768,
        #    "max_completion_tokens": None,
        #    "is_moderated": False},
        #   "per_request_limits": None},
        #  {"id": "liquid/lfm-3b",
        #   "name": "Liquid: LFM 3B"
        #  ...

    async def maybe_update_rate_limiter(self):
        if self.request_count % 100 != 0:
            return
        self.request_count += 1

        response = await self.auth_key()
        max_requests = response["rate_limit"]["requests"]

        time_window = response["rate_limit"]["interval"]
        match = re.match(r"^(\d+)s$", time_window)  # 10s
        assert match, time_window
        time_window = int(match.group(1))

        if (
                self.rate_limiter.max_requests != max_requests
                or self.rate_limiter.time_window != time_window
        ):
            logger.info(
                "Updated rate limiter max_requests=%d time_window=%d",
                max_requests, time_window
            )

        self.rate_limiter.max_requests = max_requests
        self.rate_limiter.time_window = time_window

    async def maybe_update_model_pricing(self):
        if self.model_pricing:
           return

        items = await self.models()
        for item in items:
            pricing = item["pricing"]
            pricing["prompt"] = float(pricing["prompt"])
            pricing["completion"] = float(pricing["completion"])
            self.model_pricing[item["id"]] = pricing

    def usage_cost(self, model, usage):
        pricing = self.model_pricing[model]
        return (
            usage["prompt_tokens"] * pricing["prompt"]
            + usage["completion_tokens"] * pricing["completion"]
        )

    async def __call__(self, model, instruction):
        await self.maybe_update_model_pricing()
        await self.maybe_update_rate_limiter()
        await self.rate_limiter.maybe_sleep()
        self.rate_limiter.add_request_time()

        response = await self.chat_completions(
            model=model,
            messages=[{
                "role": "user",
                "content": instruction
            }],
            temperature=0
        )

        return {
            "answer": response["choices"][0]["message"]["content"],
            "usage": response["usage"],
            "cost": self.usage_cost(model, response["usage"])
        }
