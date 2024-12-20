import uuid

from backend.conversions.conversion_interface import IConversion
from backend.errors.error import (  # Define this error
    TaskDtoToTaskEntityConversionError, TaskEntityToTaskDtoConversionError,
    TaskEntityToTaskModelConversionError, TaskModelToTaskEntityConversionError,
    UserDtoToUserEntityConversionError, UserEntityToUserDtoConversionError,
    UserEntityToUserModelConversionError, UserModelToUserEntityConversionError)
from backend.logger.logger import custom_logger
from backend.models.dto import TaskDto, UserDto
from backend.models.entitiy import TaskEntity, UserEntity
from backend.models.model import TaskModel, UserModel


class SqliteConversion(IConversion):

    def user_entity_to_model(self, user_entity: UserEntity) -> UserModel:
        """
        Converts a UserEntity to a UserModel (SQLAlchemy model)
        """
        try:
            return UserModel(
                user_id=user_entity.user_id,
                first_name=user_entity.first_name,
                last_name=user_entity.last_name,
                user_name=user_entity.user_name,
                phone=user_entity.phone,
                email=user_entity.email,
                password=user_entity.password,
            )
        except Exception as e:
            custom_logger.error(f"Error during UserEntity to UserModel conversion: {e}")
            raise UserEntityToUserModelConversionError

    def task_entity_to_model(self, task_entity: TaskEntity) -> TaskModel:
        """
        Converts a TaskEntity to a TaskModel (SQLAlchemy model)
        """
        try:
            return TaskModel(
                task_id=task_entity.task_id,
                task_title=task_entity.task_title,
                task_description=task_entity.task_description,
                task_category=task_entity.task_category,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskEntity to TaskModel conversion: {e}")
            raise TaskEntityToTaskModelConversionError

    def user_model_to_entity(self, user_model: UserModel) -> UserEntity:
        """
        Converts a UserModel to a UserEntity
        """
        try:
            return UserEntity(
                user_id=user_model.user_id,
                first_name=user_model.first_name,
                last_name=user_model.last_name,
                user_name=user_model.user_name,
                email=user_model.email,
                phone=user_model.phone,
                password=user_model.password,
            )
        except Exception as e:
            custom_logger.error(f"Error during UserModel to UserEntity conversion: {e}")
            raise UserModelToUserEntityConversionError

    def task_model_to_entity(self, task_model: TaskModel) -> TaskEntity:
        """
        Converts a TaskModel to a TaskEntity
        """
        try:
            return TaskEntity(
                task_id=task_model.task_id,
                task_title=task_model.task_title,
                task_description=task_model.task_description,
                task_category=task_model.task_category,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskModel to TaskEntity conversion: {e}")
            raise TaskModelToTaskEntityConversionError

    def user_entity_to_dto(self, user_entity: UserEntity) -> UserDto:
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
            raise UserEntityToUserDtoConversionError

    def task_entity_to_dto(self, task_entity: TaskEntity) -> TaskDto:
        """
        Converts a TaskEntity to a TaskDto (Pydantic DTO)
        """
        try:
            return TaskDto(
                task_id=task_entity.task_id,
                task_title=task_entity.task_title,
                task_description=task_entity.task_description,
                task_category=task_entity.task_category,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskEntity to TaskDto conversion: {e}")
            raise TaskEntityToTaskDtoConversionError

    def user_dto_to_entity(self, user_dto: UserDto) -> UserEntity:
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
            raise UserDtoToUserEntityConversionError

    def task_dto_to_entity(self, task_dto: TaskDto) -> TaskEntity:
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
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskDto to TaskEntity conversion: {e}")
            raise TaskDtoToTaskEntityConversionError
