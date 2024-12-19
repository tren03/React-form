import uuid
from pydantic import ValidationError
from sqlalchemy import select, and_
from sqlalchemy.exc import DuplicateColumnError, SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import (
    user_alchemy_to_pydantic,
    new_user_pydantic_to_alchemy,
)
from backend.db.db_connection import get_session
from backend.errors.error import (
    AlchemyToPydanticErr,
    DuplicateUserError,
    PydanticToAlchemyErr,
    UserNotFound,
)
from backend.logger.logger import custom_logger
from backend.models.model import PyUser as PyUser
from backend.db.migrations import User


def add_user(user_to_add: PyUser, session: Session) -> None:
    """
    Adds a user to the "user" table and session
    Accepts a pydantic user model and adds in to the database by converting to sqlalchemy model

    None - success
    rasies Exception - any error during addition

    """
    try:
        if (
            session.query(User)
            .filter(and_(User.email == user_to_add.email, User.is_deleted == False))
            .first()
        ):
            # we have a existing user
            raise DuplicateUserError

        sql_alchemy_user_to_add = new_user_pydantic_to_alchemy(user_to_add)

        session.add(sql_alchemy_user_to_add)
        session.commit()

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error converting pydantic to alc", e)
        raise e

    except DuplicateUserError as e:
        custom_logger.error("Duplicate user error while adding user ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.error("sqlalchemy error during addition of user ", e)
        raise e


def get_user_by_email(email: str) -> PyUser | None:
    """
    Gets a user by email
    return pydantic User model or error if user not found
    errors = UserNotFound,Exception
    """
    try:
        stmt = (
            select(User)
            .where(and_(User.email == email, User.is_deleted == False))
            .limit(1)
        )
        session = get_session()
        result = session.execute(stmt)
        user = result.scalars().first()
        if user:
            pydantic_user = user_alchemy_to_pydantic(user)
            if pydantic_user:
                return pydantic_user
        else:
            raise UserNotFound

    except AlchemyToPydanticErr as e:
        custom_logger.error(f"Error converting pydantic to alchemy ", e)
        raise e

    except UserNotFound as e:
        custom_logger.error(f"Login email address not found in database", e)
        raise e


def get_user_by_id(user_id: str) -> PyUser | None:
    """
    Gets a user by id
    return pydantic User model or error if user not found
    """
    try:
        stmt = (
            select(User)
            .where(and_(User.user_id == user_id, User.is_deleted == False))
            .limit(1)
        )

        session = get_session()
        result = session.execute(stmt)
        user = result.scalars().first()
        if user:
            pydantic_user = user_alchemy_to_pydantic(user)
            if pydantic_user:
                return pydantic_user
        else:
            raise UserNotFound

    except AlchemyToPydanticErr as e:
        custom_logger.error(f"Error converting pydantic to alchemy ", e)
        raise e

    except UserNotFound as e:
        custom_logger.error(f"User with given id doesnt exist", e)
        raise e
