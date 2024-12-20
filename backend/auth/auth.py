from fastapi import APIRouter, HTTPException, status

from backend.auth.auth_utils import verify_login
from backend.conversions.conversion_interface import IConversion
from backend.conversions.sqlite_conversions import SqliteConversion
from backend.db.db_connection import get_session
from backend.errors.error import CustomError, InvalidUserLogin
from backend.logger.logger import custom_logger
from backend.models.dto import LoginDetailsDto, UserDto, UserSignInDto
from backend.models.entitiy import UserEntity
from backend.repo.repo_interface import IRepo
from backend.repo.sqlite_repo import SqliteRepo

router = APIRouter()
converter: IConversion = SqliteConversion()
repo: IRepo = SqliteRepo(converter, get_session())


@router.post("/signin")
async def sign_in(user_sign_in_dto: UserSignInDto):
    """
    Handles user sign-in by attempting to add the user to the system.
    """
    try:
        user_entity = UserEntity.user_sign_in_dto_to_user_entity(user_sign_in_dto)
        repo.add_user(user_entity)

        custom_logger.info(f"user successfully signed in {user_entity} ")
        return {"message": "successful"}
    except CustomError as e:
        custom_logger.error("error while signing new user", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="err while signing new user",
        )


@router.post("/login")
async def log_in(login_dto: LoginDetailsDto):
    """
    Handles user log-in by doing auth
    """
    try:
        verify_login(login_dto, repo)
        custom_logger.info(f"user successfully logged in {login_dto} ")
        return {"message": "successful login"}
    except InvalidUserLogin as e:
        custom_logger.error("Wrong credentials", e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Server error: Could not sign in user",
        )
    except CustomError as e:
        custom_logger.error("Error while logging in ", e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Server error: Could not sign in user",
        )
