
import os

import pytest

from simple.clients.runpod import RunpodClient


@pytest.fixture
async def runpod_client():
    api_key = os.getenv("RUNPOD_API_KEY")
    assert api_key

    client = RunpodClient(api_key=api_key)
    yield client
    await client.session.close()


async def test_completions(runpod_client):
    response = await runpod_client(
        endpoint_id="mh1ykaqkens50q",
        model="MTSAIR/Cotype-Nano",
        instruction="1 + 1"
    )
    assert "2" in response["answer"]
    assert response["cost"] > 0
