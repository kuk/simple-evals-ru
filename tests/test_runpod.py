
import os

import pytest

from simple.clients.runpod import RunpodClient


@pytest.fixture
async def runpod_client():
    api_key = os.getenv("RUNPOD_API_KEY")
    assert api_key

    client = RunpodClient(api_key=api_key)
    await client.update_model_endpoints()
    yield client
    await client.session.close()


async def test_completion(runpod_client):
    response = await runpod_client(
        model="IlyaGusev/saiga_yandexgpt_8b",
        instruction="1 + 1"
    )
    assert "2" in response["answer"]
