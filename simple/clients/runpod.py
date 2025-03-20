
import aiohttp

from .common import retrying


class RunpodClient:
    def __init__(self, api_key):
        self.api_key = api_key

        self.session = aiohttp.ClientSession()
        self.model_endpoints = {}

    @retrying
    async def graphql(self, query, variables=None):
        response = await self.session.post(
            "https://api.runpod.io/graphql",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "query": query,
                "variables": variables,
            },
            timeout=aiohttp.ClientTimeout(total=30)
        )
        response.raise_for_status()
        return await response.json()

    # https://graphql-spec.runpod.io/
    async def myself_pods(self):
        data = await self.graphql("""
query myself {
  myself {
    pods {
      id
      name
      runtime {
        ports {
          ip
          isIpPublic
          privatePort
          publicPort
          type
        }
      }
    }
  }
}
""")
        return data["data"]["myself"]["pods"]

    async def update_model_endpoints(self):
        # Cloudflare proxy https://{pod_id}-8000.proxy.runpod.net/v1/chat/completions
        # https://blog.runpod.io/when-to-use-or-not-use-the-proxy-on-runpod/

        for pod_item in await self.myself_pods():
            if not pod_item["runtime"]:
                continue

            for port_item in pod_item["runtime"]["ports"]:
                if port_item["type"] == "tcp" and port_item["privatePort"] == 8000:
                    ip = port_item["ip"]
                    port = port_item["publicPort"]
                    self.model_endpoints[pod_item["name"]] = f"http://{ip}:{port}"
                    break

    @retrying
    async def chat_completions(self, model, messages, temperature=0):
        endpoint = self.model_endpoints[model]
        response = await self.session.post(
            f"{endpoint}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": 4000,
            },
            timeout=aiohttp.ClientTimeout(total=300)
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
        return await response.json()

    async def __call__(self, model, instruction):
        response = await self.chat_completions(
            model=model,
            messages=[{
                "role": "user",
                "content": instruction
            }]
        )

        return {
            "answer": response["choices"][0]["message"]["content"],
            "usage": response["usage"],
            "cost": 0
        }
