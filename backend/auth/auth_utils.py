from sqlalchemy.exc import SQLAlchemyError

from backend.errors.error import (DuplicateUserError, InvalidUserLogin,
                                  UserEntityToUserModelConversionError,
                                  UserNotFound)
from backend.logger.logger import custom_logger
from backend.models.dto import LoginDetailsDto
from backend.models.entitiy import UserEntity
from backend.repo.repo_interface import IRepo


# should return jwt for user, for now returning None
def verify_login(login_dto: LoginDetailsDto, repo: IRepo) -> None:
    """
    We check if the email and password exist in the database and are valid
    """
    try:

        user_entity = repo.get_user_by_email(login_dto.email)
        if user_entity.password != login_dto.password:
            raise InvalidUserLogin

    except InvalidUserLogin as e:
        custom_logger.error("Invalid login credentials", e)
        raise e

    except DuplicateUserError as e:
        custom_logger.error(f"Duplicate user error: {e.message()}")
        raise e

    except UserEntityToUserModelConversionError as e:
        custom_logger.error(f"Error converting UserEntity to UserModel: {e.message()}")
        raise e

    except SQLAlchemyError as e:
        custom_logger.error(f"SQLAlchemy error during addition of user: {e}")
        raise e

    except UserNotFound as e:
        custom_logger.error(f"Login email address not found in database", e)
        raise e
