from fastapi import APIRouter, HTTPException, status
from backend.db.operations import add_user
from backend.errors.error import DuplicateUserError
from backend.models.model import LoginDetails, User
from backend.db.db_connection import get_session

# from backend.model import Task
# from backend.db import get_db_conn
# import sqlite3

router = APIRouter()


@router.post("/signin")
async def sign_in(obj: User):
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
    stat = add_user(obj, get_session())
    if stat == None:
        return {"message": "successful"}

    if isinstance(stat, DuplicateUserError):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Duplicate user",
        )

    print("err while adding sigin-in : ", stat)
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Server error: Could not sign in user",
    )


@router.post("/login")
async def log_in(obj: LoginDetails):
    pass
