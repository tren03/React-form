import datetime
import os
from datetime import timedelta, timezone

import jwt
from dotenv import load_dotenv

from backend.errors.error import InvalidJWT
from backend.logger.logger import custom_logger

load_dotenv(dotenv_path="../../.env")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")


def create_jwt(user_id: str):
    expiration_time = datetime.datetime.now(tz=timezone.utc) + timedelta(minutes=40)

    payload = {
        "user_id": user_id,
        "exp": expiration_time,
    }
    custom_logger.info(f"payload : {payload}")

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    custom_logger.info(f"ENCODED : {token}")


def verify_jwt(token: str):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        print("DECODED : ", decoded)
        return decoded

    except jwt.ExpiredSignatureError as e:
        custom_logger.error(f"Token has expired {e}")
        raise InvalidJWT

    except jwt.DecodeError as e:
        print(f"Decode error : {e}")
        raise InvalidJWT

    except jwt.InvalidTokenError as e:
        print(f"Invalid token: {e}")
        raise InvalidJWT
