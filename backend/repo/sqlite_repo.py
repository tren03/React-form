from sqlalchemy import and_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from backend.errors.error import (AlchemyToPydanticErr, DuplicateUserError,
                                  TaskEntityToTaskModelConversionError,
                                  TaskNotFound,
                                  UserEntityToUserModelConversionError,
                                  UserNotFound)
from backend.logger.logger import custom_logger
from backend.models.entitiy import TaskEntity, UserEntity
from backend.models.model import TaskModel, UserModel
from backend.repo.repo_interface import IRepo


class SqliteRepo(IRepo):
    def __init__(self, conversion, session: Session):
        self.conversion = conversion
        self.session = session

    def add_user(self, user_to_add: UserEntity):
        try:
            # Check if the user already exists by email
            existing_user = self.get_user_by_email(user_to_add.email)
            if existing_user:
                raise DuplicateUserError()

            # Convert UserEntity to UserModel and add to DB
            user_model = self.conversion.user_entity_to_model(user_to_add)
            self.session.add(user_model)
            self.session.commit()
            return user_model

        except DuplicateUserError as e:
            custom_logger.error(f"Duplicate user error: {e.message()}")
            raise e

        except UserEntityToUserModelConversionError as e:
            custom_logger.error(
                f"Error converting UserEntity to UserModel: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error during addition of user: {e}")
            raise e

    def add_task(self, task_to_add: TaskEntity):
        try:
            # Convert TaskEntity to TaskModel and add to DB
            task_model = self.conversion.task_entity_to_model(task_to_add)
            self.session.add(task_model)
            self.session.commit()
            return task_model

        except TaskEntityToTaskModelConversionError as e:
            custom_logger.error(
                f"Error converting TaskEntity to TaskModel: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error during addition of task: {e}")
            raise e

    def get_user_by_id(self, user_id_to_search: str) -> UserEntity:
        try:
            stmt = select(UserModel).where(UserModel.user_id == user_id_to_search)
            result = self.session.execute(stmt)
            user = result.scalars().first()

            if user:
                return self.conversion.user_model_to_entity(user)
            else:
                raise UserNotFound()

        except UserNotFound as e:
            custom_logger.error(
                f"User not found for id {user_id_to_search}: {e.message()}"
            )
            raise e

        except AlchemyToPydanticErr as e:
            custom_logger.error(
                f"Error converting UserModel to UserEntity: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while fetching user by ID: {e}")
            raise e

    def get_task_by_id(self, task_id_to_search: str) -> TaskEntity:
        try:
            stmt = select(TaskModel).where(TaskModel.task_id == task_id_to_search)
            result = self.session.execute(stmt)
            task = result.scalars().first()

            if task:
                return self.conversion.task_model_to_entity(task)
            else:
                raise TaskNotFound()

        except TaskNotFound as e:
            custom_logger.error(
                f"Task not found for id {task_id_to_search}: {e.message()}"
            )
            raise e

        except AlchemyToPydanticErr as e:
            custom_logger.error(
                f"Error converting TaskModel to TaskEntity: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while fetching task by ID: {e}")
            raise e

    def get_user_by_email(self, user_email_to_search: str) -> UserEntity:
        try:
            stmt = select(UserModel).where(UserModel.email == user_email_to_search)
            result = self.session.execute(stmt)
            user = result.scalars().first()

            if user:
                return self.conversion.user_model_to_entity(user)
            else:
                raise UserNotFound()

        except UserNotFound as e:
            custom_logger.error(
                f"User not found for email {user_email_to_search}: {e.message()}"
            )
            raise e

        except AlchemyToPydanticErr as e:
            custom_logger.error(
                f"Error converting UserModel to UserEntity: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while fetching user by email: {e}")
            raise e

    def get_all_tasks_of_user(self, user_id_to_search: str) -> list[TaskEntity]:
        try:
            stmt = select(TaskModel).where(
                and_(
                    TaskModel.user_id == user_id_to_search,
                    TaskModel.is_deleted == False,
                )
            )
            result = self.session.execute(stmt)
            tasks = result.scalars().all()

            if tasks:
                return [self.conversion.task_model_to_entity(task) for task in tasks]
            else:
                raise TaskNotFound()

        except TaskNotFound as e:
            custom_logger.error(
                f"No tasks found for user {user_id_to_search}: {e.message()}"
            )
            raise e

        except AlchemyToPydanticErr as e:
            custom_logger.error(
                f"Error converting TaskModel to TaskEntity: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while fetching tasks for user: {e}")
            raise e

    def get_all_users(self) -> list[UserEntity]:
        try:
            stmt = select(UserModel).where(UserModel.is_deleted == False)
            result = self.session.execute(stmt)
            users = result.scalars().all()

            if users:
                return [self.conversion.user_model_to_entity(user) for user in users]
            else:
                raise UserNotFound()

        except UserNotFound as e:
            custom_logger.error(f"No users found: {e.message()}")
            raise e

        except AlchemyToPydanticErr as e:
            custom_logger.error(
                f"Error converting UserModel to UserEntity: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while fetching all users: {e}")
            raise e

    def update_task_by_id(self, task_id_to_update: str, new_task: TaskEntity):
        try:

            self.delete_task_by_id(task_id_to_update)
            self.add_task(new_task)

        except TaskNotFound as e:
            custom_logger.error(
                f"Task not found for update with ID {task_id_to_update}: {e.message()}"
            )
            raise e

        except TaskEntityToTaskModelConversionError as e:
            custom_logger.error(
                f"Error converting TaskEntity to TaskModel: {e.message()}"
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.error(f"SQLAlchemy error while updating task: {e}")
            raise e

    def delete_task_by_id(self, task_id_to_delete: str):
        try:
            task = (
                self.session.query(TaskModel)
                .filter(
                    and_(
                        TaskModel.task_id == task_id_to_delete,
                        TaskModel.is_deleted == False,
                    )
                )
                .first()
            )

            if task:
                task.is_deleted = True
                self.session.commit()
            else:
                raise TaskNotFound

        except TaskNotFound as e:
            custom_logger.error("Task not found in the database while deleting ", e)
            raise e

        except UserNotFound as e:
            custom_logger.error(
                "The user whose task needs to be added, doesnt exist : ", e
            )
            raise e

        except SQLAlchemyError as e:
            custom_logger.info(
                "Error while adding a task during sqlalchemy operation : ", e
            )
            raise e
