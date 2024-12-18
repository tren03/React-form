from backend.db.migrations import User
from backend.errors.error import AlchemyToPydanticErr, PydanticToAlchemyErr
from backend.models.model import User as PyUser
import uuid


def user_alchemy_to_pydantic(alchemy_user: User) -> PyUser | Exception:
    """
    Takes sqlalchemy user object and converts to pydantic user model
    Returns None if the conversion fails.
    """
    try:
        pydantic_user = PyUser(
            first_name=alchemy_user.first_name,
            last_name=alchemy_user.last_name,
            user_name=alchemy_user.user_name,
            phone=alchemy_user.phone,
            email=alchemy_user.email,
            password=alchemy_user.password,
        )
        return pydantic_user
    except Exception as e:
        print("somthing went wrong while conversion from alchemy to pydantic model ", e)
        return AlchemyToPydanticErr()


def user_pydantic_to_alchemy(pydantic_user: PyUser) -> User | Exception:
    """
    Takes pydantic user object and converts to sqlalchemy user model.
    Returns None if the conversion fails.
    """
    try:
        sql_alchemy_user = User(
            user_id=str(uuid.uuid4()),
            first_name=pydantic_user.first_name,
            last_name=pydantic_user.last_name,
            user_name=pydantic_user.user_name,
            phone=pydantic_user.phone,
            email=pydantic_user.email,
            password=pydantic_user.password,
        )
        return sql_alchemy_user
    except Exception as e:
        print("somthing went wrong while conversion from pydantic to alchemy model ", e)
        return PydanticToAlchemyErr()
