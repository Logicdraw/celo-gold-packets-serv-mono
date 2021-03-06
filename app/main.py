import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware


from app.api import router

from app.config.settings import settings



from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware



from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


from app.extensions import limiter


# from raven import Client


import os




async def on_startup():
	logger.info('FASTAPI APP STARTUP!')



async def on_shutdown():
	logger.info('FASTAPI APP SHUTDOWN!')





def create_app():
	# Create FastAPI app --

	app = FastAPI(
		title=settings.PROJECT_NAME,
		openapi_url=f'{settings.API_V1_STR}/openapi-a290rj10r1290By.json',
	)


	app.state_limiter = limiter
	app.add_exception_handler(
		RateLimitExceeded,
		_rate_limit_exceeded_handler,
	)

	if (settings.STAGING or settings.PRODUCTION):
		app.add_middleware(HTTPSRedirectMiddleware)
		# client_sentry = Client(settings.SENTRY_DSN)


	if settings.BACKEND_CORS_ORIGINS:
		app.add_middleware(
			CORSMiddleware,
			allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
			allow_credentials=True,
			allow_methods=['*'],
			allow_headers=['*'],
		)


	app.include_router(router)


	app.add_event_handler(
		'startup',
		on_startup,
	)

	app.add_event_handler(
		'shutdown',
		on_shutdown,
	)


	return app



app = create_app()




@app.get('/')
async def read_root():
	return {'it is...': 'working!'}






