from fastapi import APIRouter


from app.api.v1.endpoints import (
	resources,
)

from app.config.settings import settings




api_v1_router = APIRouter(
	prefix=settings.API_V1_STR,
)



api_v1_router.include_router(
	resources.router,
	prefix='/_resources',
	tags=['resources'],
)


