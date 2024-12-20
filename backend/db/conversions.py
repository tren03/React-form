from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from backend.db.migrations import UserModel
from backend.db.migrations import TaskModel
from backend.errors.error import (
    AlchemyToPydanticErr,
    PydanticToAlchemyErr,
)
from backend.models.dto import UserDto,TaskDto
from backend.logger.logger import custom_logger
import uuid


def user_alchemy_to_pydantic(alchemy_user: UserModel) -> UserDto | None:
    """
    Takes sqlalchemy user object and converts to pydantic user model
    Returns custom error - AlchemyToPydanticErr if the conversion fails.
    """
    try:
        pydantic_user = UserDto(
            first_name=alchemy_user.first_name,
            last_name=alchemy_user.last_name,
            user_name=alchemy_user.user_name,
            phone=alchemy_user.phone,
            email=alchemy_user.email,
            password=alchemy_user.password,
        )
        return pydantic_user
    except ValidationError as e:
        custom_logger.error(
            "somthing went wrong while conversion of user from alchemy to pydantic model ",
            e,
        )
        raise AlchemyToPydanticErr


def new_user_pydantic_to_alchemy(pydantic_user: UserDto) -> UserModel | None:
    """
    Takes pydantic user object and converts to sqlalchemy user model and returns a new PyUser object
    raises custom error - PydanticToAlchemyErr if the conversion fails.
    """
    try:
        sql_alchemy_user = UserModel(
            user_id=str(uuid.uuid4()),
            first_name=pydantic_user.first_name,
            last_name=pydantic_user.last_name,
            user_name=pydantic_user.user_name,
            phone=pydantic_user.phone,
            email=pydantic_user.email,
            password=pydantic_user.password,
        )
        return sql_alchemy_user
    except SQLAlchemyError as e:
        custom_logger.info("Error during conversion of pydantic to alchemy model ", e)
        raise PydanticToAlchemyErr


# to work on
# def existing_user_pydantic_to_alchemy(pydantic_user: PyUser) -> User | Exception:
#     """
#     Takes pydantic user object and converts to sqlalchemy user model and returns a PyUser object which exisits in the database
#     errors = UserNotFound, Exception
#     """
#     try:
#         verified_pydantic_user = get_user_by_email(pydantic_user.email)
#         if isinstance(verified_pydantic_user, Exception):
#             raise verified_pydantic_user
#
#         return User()
#
#     except UserNotFound as e:
#         print(f"Login email address not found in database", e)
#         return e
#     except Exception as e:
#         print(
#             "somthing went wrong while conversion of user from pydantic to alchemy model ",
#             e,
#         )
#         return PydanticToAlchemyErr()
#


def task_alchemy_to_pydantic(alchemy_task: TaskModel) -> TaskDto:
    """
    Takes sqlalchemy task object and converts to pydantic task model
    error AlchemyToPydanticErr
    """
    try:
        pydantic_task = TaskDto(
            task_title=alchemy_task.task_title,
            task_description=alchemy_task.task_description,
            task_category=alchemy_task.task_category,
        )
        return pydantic_task
    except ValidationError as e:
        custom_logger.error(
            "somthing went wrong while conversion of Task from alchemy to pydantic model ",
            e,
        )
        raise AlchemyToPydanticErr


def new_task_pydantic_to_alchemy(pydantic_task: TaskDto, user_id: str) -> TaskModel:
    """
    Takes pydantic task object and user_id(foreign key) and converts to sqlalchemy task model.
    Returns custom error - PydanticToAlchemyErr if the conversion fails.
    """
    try:
        sql_alchemy_task = TaskModel(
            task_id=str(uuid.uuid4()),
            task_title=pydantic_task.task_title,
            task_description=pydantic_task.task_description,
            task_category=pydantic_task.task_category,
            user_id=user_id,
        )
        return sql_alchemy_task
    except SQLAlchemyError as e:
        custom_logger.error(
            "somthing went wrong while conversion of Task from pydantic to alchemy model ",
            e,
        )
        raise PydanticToAlchemyErr
