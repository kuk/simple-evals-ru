
import time
import asyncio

import aiohttp

from .common import retrying


# https://www.runpod.io/pricing
MODEL_PRICING = {
    "MTSAIR/Cotype-Nano": 0.00011,
    "t-tech/T-lite-it-1.0": 0.00013,
    "t-tech/T-pro-it-1.0": 0.00060,
}


def runpod_duration_cost(model, duration):
    return duration * MODEL_PRICING[model]


class RunpodClient:
    def __init__(self, api_key):
        self.api_key = api_key

        self.session = aiohttp.ClientSession()
        self.semaphore = asyncio.Semaphore(5)

    @retrying
    async def completions(self, endpoint_id, model, messages, temperature=0, max_tokens=2000):
        async with self.semaphore:
            response = await self.session.post(
                f"https://api.runpod.ai/v2/{endpoint_id}/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens
                },
                timeout=aiohttp.ClientTimeout(total=600)
            )

            # {
            #   "choices": [
            #     {
            #       "finish_reason": "stop",
            #       "index": 0,
            #       "logprobs": null,
            #       "message": {
            #         "content": "It seems like your ...ured and precise answer.",
            #         "role": "assistant",
            #         "tool_calls": []
            #       },
            #       "stop_reason": null
            #     }
            #   ],
            #   "created": 1740324853,
            #   "id": "chatcmpl-6f3b0089eb22459a8a63da786ffa7c3f",
            #   "model": "MTSAIR/Cotype-Nano",
            #   "object": "chat.completion",
            #   "prompt_logprobs": null,
            #   "usage": {
            #     "completion_tokens": 49,
            #     "prompt_tokens": 8,
            #     "prompt_tokens_details": null,
            #     "total_tokens": 57
            #   }
            # }

            response.raise_for_status()
            data =  await response.json()

            if "choices" not in data:
                print(data)

                raise aiohttp.ClientError(str(data))

            return data


    async def __call__(self, endpoint_id, model, instruction):
        start = time.monotonic()
        response = await self.completions(
            endpoint_id=endpoint_id,
            model=model,
            messages=[{
                "role": "user",
                "content": instruction
            }]
        )
        duration = time.monotonic() - start

        return {
            "answer": response["choices"][0]["message"]["content"],
            "usage": response["usage"],
            "duration": duration,
            "cost": runpod_duration_cost(model, duration)
        }
