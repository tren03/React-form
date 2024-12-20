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
                user_id=task_model.user_id,
            )
        except Exception as e:
            custom_logger.error(f"Error during TaskModel to TaskEntity conversion: {e}")
            raise TaskModelToTaskEntityConversionError
