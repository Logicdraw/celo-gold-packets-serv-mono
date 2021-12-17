from fastapi import APIRouter


# from app.api.health import router as health_router
from app.api.v1.api import api_v1_router


router = APIRouter()

router.include_router(api_v1_router)
# router.include_router(health_router)

