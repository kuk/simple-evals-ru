
import os

import pytest

from simple.clients.gigachat import GigachatClient


@pytest.fixture
async def gigachat_client():
    secret = os.getenv("GIGACHAT_SECRET")
    assert secret

    client = GigachatClient(secret=secret)
    yield client
    await client.session.close()


async def test_completion(gigachat_client):
    response = await gigachat_client("GigaChat", "1 + 1")
    assert "2" in response["answer"]
    assert response["cost"] > 0
