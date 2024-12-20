from backend.auth.jwt_utils import create_jwt
from backend.db.user_operations import get_user_by_email
from backend.errors.error import (AlchemyToPydanticErr, InvalidUserLogin,
                                  UserNotFound)
from backend.logger.logger import custom_logger
from backend.models.dto import LoginDetailsDto


# should return jwt for user, for now returning None
def verify_login(obj: LoginDetailsDto) -> None:
    """
    We check if the email and password exist in the database and are valid
    """
    try:

        pydantic_user = get_user_by_email(obj.email)
        if pydantic_user:
            if obj.password != pydantic_user.password:
                raise InvalidUserLogin

    except InvalidUserLogin as e:
        custom_logger.error("Invalid login credentials", e)
        raise e

    except AlchemyToPydanticErr as e:
        custom_logger.error(f"Error converting pydantic to alchemy ", e)
        raise e

    except UserNotFound as e:
        custom_logger.error(f"Login email address not found in database", e)
        raise e
