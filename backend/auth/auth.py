from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_200_OK

from backend.auth.auth_utils import verify_login
from backend.auth.jwt_utils import get_current_user
from backend.errors.error import (CustomError, DuplicateUserError,
                                  InvalidUserLogin, UserNotFound)
from backend.logger.logger import custom_logger
from backend.models.dto import (LoginDetailsDto, TokenDto, UserDto,
                                UserSignInDto)
from backend.models.entitiy import UserEntity
from backend.repo.current_repo import get_repo

router = APIRouter()
repo = get_repo()


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
    except DuplicateUserError as e:
        custom_logger.error(e.message())
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message(),
        )

    except CustomError as e:
        custom_logger.error("error while signing new user", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="err while signing new user",
        )


@router.post(
    "/token",
    summary="Create access token for user",
    response_model=TokenDto,
)
async def log_in(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Handles user log-in by doing auth and returnint access token
    """
    try:
        login_dto = LoginDetailsDto(
            email=form_data.username, password=form_data.password
        )
        access_token = verify_login(login_dto, repo)
        custom_logger.info(f"user successfully logged in {login_dto} ")
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=False,
            path="/",
            samesite="lax",
        )
        return {"access_token": ":)"}

    except UserNotFound as e:
        custom_logger.error(f"Invalid login attempt: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found in the database",
        )

    except InvalidUserLogin as e:
        custom_logger.error(f"Invalid login attempt: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please check your email and password and try again.",
        )

    except CustomError as e:
        custom_logger.error(f"Unexpected error during login: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurred while processing your login. Please try again later.",
        )


@router.get("/items/me")
async def read_items(user_id: Annotated[str, Depends(get_current_user)]):
    return {"user_id": user_id}
