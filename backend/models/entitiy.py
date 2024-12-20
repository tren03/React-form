import uuid

from pydantic import BaseModel

from backend.errors.error import (  # Define this error
    TaskDtoToTaskEntityConversionError, TaskEntityToTaskDtoConversionError,
    UserDtoToUserEntityConversionError, UserEntityToUserDtoConversionError)
from backend.logger.logger import custom_logger
from backend.models.dto import TaskDto, UserDto


class JWTInfoEntity(BaseModel):
    user_id: str
    email: str


class UserEntity(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    user_name: str
    email: str
    phone: str
    password: str

    @staticmethod
    def user_entity_to_dto(user_entity: "UserEntity") -> UserDto:
        """
        Converts a UserEntity to a UserDto (Pydantic DTO)
        """
        try:
            return UserDto(
                user_id=user_entity.user_id,
                first_name=user_entity.first_name,
                last_name=user_entity.last_name,
                user_name=user_entity.user_name,
                email=user_entity.email,
                phone=user_entity.phone,
                password=user_entity.password,
            )
        except Exception as e:
            custom_logger.error(f"Error during UserEntity to UserDto conversion: {e}")
            raise UserEntityToUserDtoConversionError()

    @staticmethod
    def user_dto_to_entity(user_dto: UserDto) -> "UserEntity":
        """
        Converts a UserDto (Pydantic DTO) to a UserEntity
        """
        try:
            if not user_dto.user_id:
                generated_user_id = str(uuid.uuid4())
            else:
                generated_user_id = user_dto.user_id
            return UserEntity(
                user_id=generated_user_id,
                first_name=user_dto.first_name,
                last_name=user_dto.last_name,
                user_name=user_dto.user_name,
                email=user_dto.email,
                phone=user_dto.phone,
                password=user_dto.password,
            )
        except Exception as e:
            custom_logger.error(f"Error during UserDto to UserEntity conversion: {e}")
            raise UserDtoToUserEntityConversionError()


class TaskEntity(BaseModel):
    task_id: str
    task_title: str
    task_description: str
    task_category: str
    user_id: str

    @staticmethod
    def task_entity_to_dto(task_entity: "TaskEntity") -> TaskDto:
        """
        Converts a TaskEntity to a TaskDto (Pydantic DTO)
        """
        try:
            return TaskDto(
                task_id=task_entity.task_id,
                task_title=task_entity.task_title,
                task_description=task_entity.task_description,
                task_category=task_entity.task_category,
                user_id=task_entity.user_id,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskEntity to TaskDto conversion: {e}")
            raise TaskEntityToTaskDtoConversionError()

    @staticmethod
    def task_dto_to_entity(task_dto: TaskDto) -> "TaskEntity":
        """
        Converts a TaskDto (Pydantic DTO) to a TaskEntity
        """
        try:
            if not task_dto.task_id:
                generated_task_id = str(uuid.uuid4())
            else:
                generated_task_id = task_dto.task_id
            return TaskEntity(
                task_id=generated_task_id,
                task_title=task_dto.task_title,
                task_description=task_dto.task_description,
                task_category=task_dto.task_category,
                user_id=task_dto.user_id,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskDto to TaskEntity conversion: {e}")
            raise TaskDtoToTaskEntityConversionError()
