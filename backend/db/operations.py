import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.models.model import User as PyUser
from backend.db.migrations import User


def add_user(user_to_add: PyUser, session: Session) -> int:
    """
    Adds a user to the "user" table and session
    Accepts a pydantic user model and adds in to the database by converting to sqlalchemy model
    returns
    0 = success
    1 = IntegrityError -> duplicate user addition
    2 = general error
    """
    try:
        print(uuid.uuid4())
        if session.query(User).filter(User.email == user_to_add.email).first():
            # we have a existing user
            print("existing user addition error")
            return 1
        sql_alchemy_user_to_add = User(
            user_id=str(uuid.uuid4()),
            first_name=user_to_add.first_name,
            last_name=user_to_add.last_name,
            user_name=user_to_add.user_name,
            phone=user_to_add.phone,
            email=user_to_add.email,
            password=user_to_add.password,
        )
        session.add(sql_alchemy_user_to_add)
        session.commit()

    except SQLAlchemyError as e:
        print(f"exception during user creation {e}")
        return 2
    return 0
