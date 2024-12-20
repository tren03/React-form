from abc import ABC, abstractmethod

from backend.models.dto import TaskDto, UserDto
from backend.models.entitiy import TaskEntity, UserEntity
from backend.models.model import TaskModel, UserModel


class IConversion(ABC):
    @abstractmethod
    def user_entity_to_model(self, user_entity: UserEntity) -> UserModel:
        pass

    @abstractmethod
    def task_entity_to_model(self, task_entity: TaskEntity) -> TaskModel:
        pass

    @abstractmethod
    def user_model_to_entity(self, user_model: UserModel) -> UserEntity:
        pass

    @abstractmethod
    def task_model_to_entity(self, task_model: TaskModel) -> TaskEntity:
        pass
