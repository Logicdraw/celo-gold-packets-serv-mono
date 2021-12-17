import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



from datetime import (
	datetime,
	timedelta,
)

from typing import (
	Any,
	Union,
	Optional,
)


from jose import jwt

from passlib.context import CryptContext


from app.config.settings import settings





pwd_context = CryptContext(
	schemes=["bcrypt"],
	deprecated="auto",
)


ALGORITHM = 'HS256'




def create_token(
	subject: Union[str, Any],
	expires_delta: timedelta = None,
	not_before_dt: datetime = None,
) -> str:
	# Create token --

	data = {
		'sub': str(subject),
	}

	if expires_delta:
		data['exp'] = expires_delta

	if not_before_dt:
		data['nbf'] = not_before_dt


	encoded_jwt = jwt.encode(
		data,
		settings.SECRET_KEY.get_secret_value(),
		algorithm='HS256',
	)

	return encoded_jwt


def verify_token(
	token: str
) -> Optional[str]:
	# Verify Token --

	try:
		decoded_token = jwt.decode(
			token,
			settings.SECRET_KEY.get_secret_value(),
			algorithms=["HS256"],
		)
		return decoded_token["sub"]
	except jwt.JWTError:
		return None



