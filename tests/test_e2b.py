
import os

import pytest

from simple.clients.e2b import E2BClient


@pytest.fixture
async def e2b_client():
    api_key = os.getenv("E2B_API_KEY")
    assert api_key

    client = E2BClient(api_key=api_key)
    yield client
    await client.session.close()


async def test_assert_false(e2b_client):
    response = await e2b_client("assert False", timeout=5)
    assert response["traceback"]


async def test_timeout(e2b_client):
    response = await e2b_client("from time import sleep; sleep(10)", timeout=1)
    assert response["timed_out"]
