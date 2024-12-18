from sqlite3 import Error
import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import user_pydantic_to_alchemy
from backend.errors.error import DuplicateUserError
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

        # sql_alchemy_user_to_add = User(
        #     user_id=str(uuid.uuid4()),
        #     first_name=user_to_add.first_name,
        #     last_name=user_to_add.last_name,
        #     user_name=user_to_add.user_name,
        #     phone=user_to_add.phone,
        #     email=user_to_add.email,
        #     password=user_to_add.password,
        # )
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


def get_user_by_email(email: str):
    """
    Gets a user by email

    """
    pass
