
import time
import asyncio
import uuid

import aiohttp

from .common import retrying


# https://developers.sber.ru/docs/ru/gigachat/api/tariffs
GIGACHAT_MODEL_PRICING = {
    "GigaChat": 1000 / 5_000_000,
    "GigaChat-Pro": 1500 / 1_000_000,
    "GigaChat-Max": 1950 / 1_000_000,
}


def gigachat_usage_cost(model, usage):
    return usage["total_tokens"] * GIGACHAT_MODEL_PRICING[model]


class GigachatClient:
    def __init__(self, secret):
        self.secret = secret
        self.session = aiohttp.ClientSession(
            # https://developers.sber.ru/docs/ru/gigachat/certificates
            connector=aiohttp.TCPConnector(ssl=False)
        )
        self.token = None
        self.expires_at = None

        # https://developers.sber.ru/docs/ru/gigachat/limitations
        self.completions_semaphore = asyncio.Semaphore(1)
        self.oauth_lock = asyncio.Lock()

    @retrying
    async def oauth(self):
        response = await self.session.post(
            "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
            headers={
                "Authorization": f"Basic {self.secret}",
                "RqUID": str(uuid.uuid4()),
            },
            data={"scope": "GIGACHAT_API_PERS"},
            timeout=aiohttp.ClientTimeout(total=10),
        )

        # {"code":4,"message":"Can"t decode "Authorization" header"}
        # {"code":1,"message":"scope data format invalid"}
        # {"access_token":"eyJjdHk...","expires_at":1705848955469}

        response.raise_for_status()
        return await response.json()

    async def maybe_oauth(self):
        async with self.oauth_lock:
            if not self.token or time.monotonic() >= self.expires_at:
                data = await self.oauth()
                self.token = data["access_token"]
                self.expires_at = data["expires_at"] / 1000

    @retrying
    async def completions(self, model, messages, temperature=0, max_tokens=16000):
        # curl "https://gigachat.devices.sberbank.ru/api/v1/chat/completions" \
        # -H "Content-Type: application/json" \
        # -H "Accept: application/json" \
        # -H "Authorization: Bearer token" \
        # --data-raw "{
        #   "model": "GigaChat:latest",
        #   "messages": [
        #     {
        #       "role": "user",
        #       "content": "Привет! Как думаешь, когда мы выпустим GigaChat?"
        #     }
        #   ],
        #   "temperature": 0.87,
        #   "top_p": 0.47,
        #   "n": 1,
        #   "stream": false,
        #   "max_tokens": 512,
        #   "repetition_penalty": 1.07,
        #   "update_interval": 0
        # }"

        async with self.completions_semaphore:
            response = await self.session.post(
                "https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
                headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}"
                },
                json={
                    "model": model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "stream": False,
                },
                timeout=aiohttp.ClientTimeout(total=120),
            )

            # {"choices": [{"message": {"content": "$1 + 1 = 2$.", "role": "assistant"},
            #               "index": 0,
            #               "finish_reason": "stop"}],
            #  "created": 1737888295,
            #  "model": "GigaChat-Pro:1.0.26.20",
            #  "object": "chat.completion",
            #  "usage": {"prompt_tokens": 15, "completion_tokens": 10, "total_tokens": 25}}

            response.raise_for_status()
            return await response.json()

    async def __call__(self, model, instruction):
        await self.maybe_oauth()
        response = await self.completions(
            model=model,
            messages=[{
                "role": "user",
                "content": instruction
            }]
        )

        return {
            "answer": response["choices"][0]["message"]["content"],
            "usage": response["usage"],
            "cost": gigachat_usage_cost(model, response["usage"])
        }
