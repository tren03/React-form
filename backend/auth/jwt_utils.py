import datetime
import os
from datetime import timedelta, timezone
from typing import Annotated

import jwt
from dotenv import load_dotenv
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from backend.errors.error import ExpiredJWT, InvalidJWT
from backend.logger.logger import custom_logger
from backend.repo.current_repo import get_repo
from backend.repo.repo_interface import IRepo

load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")


def create_jwt(user_id: str) -> str:
    expiration_time = datetime.datetime.now(tz=timezone.utc) + timedelta(minutes=40)

    payload = {
        "user_id": user_id,
        "exp": expiration_time,
    }
    custom_logger.info(f"payload : {payload}")
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    custom_logger.info(f"ENCODED : {token}")
    return token


def verify_jwt(token: str) -> dict:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        print("DECODED : ", decoded)
        return decoded

    except jwt.ExpiredSignatureError as e:
        custom_logger.error(f"Token has expired {e}")
        raise ExpiredJWT

    except jwt.DecodeError as e:
        print(f"Decode error : {e}")
        raise InvalidJWT

    except jwt.InvalidTokenError as e:
        print(f"Invalid token: {e}")
        raise InvalidJWT


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    repo: Annotated[IRepo, Depends(get_repo)],
) -> dict:
    payload = verify_jwt(token)
    # repo = get_repo()
    print(payload)
    return payload
    # need to get current user from the id
