import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



import pytest

import asyncio

from typing import (
	Dict,
	Generator,
)


from app.config.settings import settings


from asgi_lifespan import LifespanManager

from httpx import AsyncClient


from app.main import app



# --



# -- !


@pytest.fixture(scope='session', autouse=True)
def event_loop():
	"""Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
	loop = asyncio.get_event_loop_policy().new_event_loop()
	yield loop
	loop.close()



@pytest.fixture()
async def client():
	async with AsyncClient(app=app, base_url='http://test') as ac, LifespanManager(app):
		yield ac





