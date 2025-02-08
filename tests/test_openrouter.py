
import os

import pytest

from simple.clients.openrouter import OpenrouterClient


@pytest.fixture
async def openrouter_client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    assert api_key

    client = OpenrouterClient(api_key=api_key)
    yield client
    await client.session.close()


async def test_completion(openrouter_client):
    response = await openrouter_client("google/gemini-2.0-flash-001", "1 + 1")
    assert "2" in response["answer"]
    assert response["cost"] > 0
