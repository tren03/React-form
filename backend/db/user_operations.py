import uuid
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import user_alchemy_to_pydantic, user_pydantic_to_alchemy
from backend.db.db_connection import get_session
from backend.errors.error import DuplicateUserError, UserNotFound
from backend.models.model import User as PyUser
from backend.db.migrations import User


def add_user(user_to_add: PyUser, session: Session) -> None | Exception:
    """
    Adds a user to the "user" table and session
    Accepts a pydantic user model and adds in to the database by converting to sqlalchemy model

    return:
    None - success
    Exception - any error during addition

    """
    try:
        print(uuid.uuid4())
        if session.query(User).filter(User.email == user_to_add.email).first():
            # we have a existing user
            raise DuplicateUserError

        sql_alchemy_user_to_add = user_pydantic_to_alchemy(user_to_add)
        if isinstance(sql_alchemy_user_to_add, Exception):
            raise sql_alchemy_user_to_add
        session.add(sql_alchemy_user_to_add)
        session.commit()

    except DuplicateUserError as e:
        print(f"DuplicateUserError {e}")
        return e

    except SQLAlchemyError as e:
        print(f"exception during user creation {e}")
        return e

    except Exception as e:
        print(f"something went wrong in addition of user during sign in ", e)
        return e


def get_user_by_email(email: str) -> PyUser | Exception:
    """
    Gets a user by email
    return pydantic User model or error if user not found
    """
    try:
        stmt = select(User).where(User.email == email).limit(1)
        session = get_session()
        result = session.execute(stmt)
        user = result.scalars().first()
        if user:
            return user_alchemy_to_pydantic(user)
        else:
            raise UserNotFound
    except UserNotFound as e:
        print(f"Login email address not found in database", e)
        return e
    except Exception as e:
        print(f"Something went wrong while getting email of user for login checking", e)
        return e
