
import json
import time
import asyncio

import aiohttp

from .common import (
    RateLimiter,
    retrying
)


# https://e2b.dev/pricing
E2B_PRICING = 0.000028


class E2BClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=5)
        )
        # https://e2b.dev/pricing
        self.sandboxes_semaphore = asyncio.Semaphore(20)

        # FIX? Actual rate limites are unknown
        self.requests_rate_limit = RateLimiter(10, 1)

    @retrying
    async def create_sandbox(self, timeout=60, template_id="code-interpreter-v1"):
        await self.requests_rate_limit.wait()
        response = await self.session.post(
            "https://api.e2b.dev/sandboxes",
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": self.api_key
            },
            json={
                "templateID": template_id,
                "timeout": timeout
            },
        )

        # {'alias': 'code-interpreter-v1',
        #  'clientID': 'f0a76b66',
        #  'envdVersion': '0.1.5',
        #  'sandboxID': 'i7yuhw8kupcc6f0u042t2',
        #  'templateID': 'nlhz8vlwyupq845jsdg9'}

        response.raise_for_status()
        return await response.json()

    @retrying
    async def kill(self, sandbox_id):
        await self.requests_rate_limit.wait()
        response = await self.session.delete(
            f"https://api.e2b.dev/sandboxes/{sandbox_id}",
            headers={
                "X-API-KEY": self.api_key
            },
        )
        if response.status == 404:
            return
        response.raise_for_status()

    @retrying
    async def run_code(
            self, client_id, sandbox_id, code,
            language="python",
            timeout=10,
            port=49999
    ):
        await self.requests_rate_limit.wait()
        response = await self.session.post(
            f"https://{port}-{sandbox_id}-{client_id}.e2b.dev/execute",
            headers={
                "Content-Type": "application/json",
                "X-API-KEY": self.api_key
            },
            json={
                "code": code,
                "language": language,
            },
            timeout=aiohttp.ClientTimeout(
                sock_connect=5,
                sock_read=timeout
            )
        )

        # {'type': 'number_of_executions', 'execution_count': 1}
        # {"type": "result", "text": "2", "extra": {}, "is_main_result": true}
        # {'type': 'stdout', 'text': '123\n', 'timestamp': '2025-02-08T08:37:22.926533+00:00'}
        # {'type': 'error', 'name': 'ZeroDivisionError', 'value': 'division by zero', 'traceback': "-----------------------... zero"}
        # {'type': 'end_of_execution'}

        response.raise_for_status()
        results = []
        try:
            async for line in response.content:
                data = json.loads(line)
                results.append(data)
        except TimeoutError:
            pass
        return results

    async def __call__(self, code, timeout=10):
        result = {
            "execution": None,
            "result": None,
            "traceback": None,
            "timed_out": None,
            "duration": 0,
            "cost": 0
        }

        async with self.sandboxes_semaphore:
            response = await self.create_sandbox(timeout=timeout)
            client_id = response["clientID"]
            sandbox_id = response["sandboxID"]

            try:
                start = time.monotonic()
                result["execution"] = await self.run_code(
                    client_id=client_id,
                    sandbox_id=sandbox_id,
                    code=code,
                    timeout=timeout
                )
                result["duration"] = time.monotonic() - start
                result["cost"] = result["duration"] * E2B_PRICING

            finally:
                await self.kill(sandbox_id)

        result["timed_out"] = True
        for item in result["execution"]:
            if item["type"] == "result":
                result["result"] = item["text"]
            elif item["type"] == "error":
                result["traceback"] = item["traceback"]
            elif item["type"] == "end_of_execution":
                result["timed_out"] = False

        return result

