
import asyncio

import aiohttp

from .common import retrying


# https://yandex.cloud/ru/docs/foundation-models/pricing#pricing-generating
YANDEXGPT_MODEL_PRICING = {
    "yandexgpt-lite": 0.20 / 1000,
    "yandexgpt": 1.20 / 1000,
    "llama-lite": 0.20 / 1000,
    "llama": 1.20 / 1000,
}


def yandexgpt_usage_cost(model, usage):
    # https://yandex.cloud/ru/docs/foundation-models/concepts/yandexgpt/models#generation
    # yandexgpt-lite/deprecated
    # yandexgpt/latest
    model_family, _ = model.split("/", 1)
    return usage["totalTokens"] * YANDEXGPT_MODEL_PRICING[model_family]


class YandexgptClient:
    def __init__(self, api_key, folder_id):
        self.api_key = api_key
        self.folder_id = folder_id
        self.session = aiohttp.ClientSession()

        # https://yandex.cloud/ru/docs/foundation-models/concepts/limits#yandexgpt-quotas
        self.semaphore = asyncio.Semaphore(10)

    @retrying
    async def completion(self, model, messages, temperature=0, max_tokens=4000):
        # https://yandex.cloud/ru/docs/foundation-models/text-generation/api-ref/TextGeneration/completion

        async with self.semaphore:
            response = await self.session.post(
                "https://llm.api.cloud.yandex.net/foundationModels/v1/completion",
                headers={
                    "Authorization": f"Api-Key {self.api_key}",
                },
                json={
                    "modelUri": f"gpt://{self.folder_id}/{model}",
                    "completionOptions": {
                        "stream": False,
                        "temperature": temperature,
                        "maxTokens": max_tokens,
                    },
                    "messages": messages
                },
                timeout=aiohttp.ClientTimeout(total=300)
            )
            response.raise_for_status()
            data = await response.json()

        # {
        #   "error": {
        #     "grpcCode": 3,
        #     "httpCode": 400,
        #     "message": "Error in session internal_id=...",
        #     "httpStatus": "Bad Request",
        #     "details": []
        #   }
        # }

        # {
        #   "result": {
        #     "alternatives": [
        #       {
        #         "message": {
        #           "role": "assistant",
        #           "text": ""
        #         },
        #         "status": "ALTERNATIVE_STATUS_FINAL"
        #       }
        #     ],
        #     "usage": {
        #       "inputTextTokens": "16",
        #       "completionTokens": "1",
        #       "totalTokens": "17"
        #     },
        #     "modelVersion": "08.12.2023"
        #   }
        # }
        return data["result"]

    async def __call__(self, model, instruction):
        response = await self.completion(
            model=model,
            messages=[{
                "role": "user",
                "text": instruction
            }]
        )

        usage = response["usage"]
        for key in ["inputTextTokens", "completionTokens", "totalTokens"]:
            usage[key] = int(usage[key])

        return {
            "answer": response["alternatives"][0]["message"]["text"],
            "usage": usage,
            "cost": yandexgpt_usage_cost(model, usage)
        }
