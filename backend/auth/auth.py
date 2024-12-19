from fastapi import APIRouter, HTTPException, status
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from backend.auth.auth_utils import verify_login
from backend.auth.jwt_utils import create_jwt
from backend.db.user_operations import add_user, get_user_by_email
from backend.errors.error import CustomError, DuplicateUserError, UserNotFound
from backend.models.model import JWTInfo, LoginDetails, PyUser
from backend.db.db_connection import get_session
from backend.logger.logger import custom_logger

# from backend.model import Task
# from backend.db import get_db_conn
# import sqlite3

router = APIRouter()


@router.post("/signin")
async def sign_in(obj: PyUser):
    """
    Handles user sign-in by attempting to add the user to the system.

    Args:
        obj (User): The user object containing the user's credentials and other necessary data.

    Returns:
        200 response for successful signin

    Raises:
        409 duplicate user
        401 Internal server error
    """
    try:
        add_user(obj, get_session())
        custom_logger.info(f"user successfully signed in {obj} ")
        return {"message": "successful"}
    except CustomError as e:
        custom_logger.error("error while signing new user", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="err while signing new user",
        )


@router.post("/login")
async def log_in(obj: LoginDetails):
    """
    Handles user log-in by returning a jwt if verified

    Args:
        obj (LoginDetails) : Contains the email and password of the login attempt

    Returns:
        jwt token(need work)

    Raises:
        403 login failure

    """
    try:
        verify_login(obj)
        custom_logger.info(f"user successfully logged in {obj} ")
        return {"message": "successful login"}
    except CustomError as e:
        custom_logger.error("Error while logging in ", e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Server error: Could not sign in user",
        )
