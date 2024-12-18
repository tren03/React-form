from backend.db.migrations import User
from backend.db.migrations import Task
from backend.errors.error import AlchemyToPydanticErr, PydanticToAlchemyErr
from backend.models.model import User as PyUser
from backend.models.model import Task as PyTask
import uuid


def user_alchemy_to_pydantic(alchemy_user: User) -> PyUser | Exception:
    """
    Takes sqlalchemy user object and converts to pydantic user model
    Returns custom error - AlchemyToPydanticErr if the conversion fails.
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
        print(
            "somthing went wrong while conversion of user from alchemy to pydantic model ",
            e,
        )
        return AlchemyToPydanticErr()


def user_pydantic_to_alchemy(pydantic_user: PyUser) -> User | Exception:
    """
    Takes pydantic user object and converts to sqlalchemy user model.
    Returns custom error - PydanticToAlchemyErr if the conversion fails.
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
        print(
            "somthing went wrong while conversion of user from pydantic to alchemy model ",
            e,
        )
        return PydanticToAlchemyErr()


def task_alchemy_to_pydantic(alchemy_task: Task) -> PyTask | Exception:
    """
    Takes sqlalchemy task object and converts to pydantic task model
    Returns custom Exception - AlchemyToPydanticErr if the conversion fails.
    """
    try:
        pydantic_task = PyTask(
            task_title=alchemy_task.task_title,
            task_description=alchemy_task.task_description,
            task_category=alchemy_task.task_category,
        )
        return pydantic_task
    except Exception as e:
        print(
            "somthing went wrong while conversion of Task from alchemy to pydantic model ",
            e,
        )
        return AlchemyToPydanticErr()


def task_pydantic_to_alchemy(pydantic_task: PyTask, user_id: str) -> Task | Exception:
    """
    Takes pydantic task object and user_id(foreign key) and converts to sqlalchemy task model.
    Returns custom error - PydanticToAlchemyErr if the conversion fails.
    """
    try:
        sql_alchemy_task = Task(
            task_id=str(uuid.uuid4()),
            task_title=pydantic_task.task_title,
            task_description=pydantic_task.task_description,
            task_category=pydantic_task.task_category,
            user_id=user_id,
        )
        return sql_alchemy_task
    except Exception as e:
        print(
            "somthing went wrong while conversion of Task from pydantic to alchemy model ",
            e,
        )
        return PydanticToAlchemyErr()
