from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from backend.conversions.conversion_interface import IConversion
from backend.models.entitiy import TaskEntity, UserEntity


class IRepo(ABC):
    @abstractmethod
    def __init__(self, conversion: IConversion, session: Session):
        pass

    @abstractmethod
    def add_user(self, user_to_add: UserEntity):
        pass

    @abstractmethod
    def add_task(self, task_to_add: TaskEntity):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id_to_search: str) -> UserEntity:
        pass

    @abstractmethod
    def get_task_by_id(self, task_id_to_search: str) -> TaskEntity:
        pass

    @abstractmethod
    def get_user_by_email(self, user_email_to_search: str) -> UserEntity:
        pass

    @abstractmethod
    def get_all_tasks_of_user(self, user_id_to_search: str) -> list[TaskEntity]:
        pass

    @abstractmethod
    def get_all_users(self) -> list[UserEntity]:
        pass

    @abstractmethod
    def update_task_by_id(self, task_id_to_update: str, new_task: TaskEntity):
        pass

    @abstractmethod
    def delete_task_by_id(self, task_id_to_delete: str):
        pass
