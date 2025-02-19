
import os

import pytest

from simple.clients.yandexgpt import YandexgptClient


@pytest.fixture
async def yandexgpt_client():
    api_key = os.getenv("YANDEXGPT_API_KEY")
    folder_id = os.getenv("YANDEXGPT_FOLDER_ID")
    assert api_key
    assert folder_id

    client = YandexgptClient(api_key=api_key, folder_id=folder_id)
    yield client
    await client.session.close()


async def test_completion(yandexgpt_client):
    response = await yandexgpt_client("yandexgpt-lite/latest", "1 + 1")
    assert "2" in response["answer"]
    assert response["cost"] > 0

