from sqlalchemy import and_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import (
    task_alchemy_to_pydantic,
    new_task_pydantic_to_alchemy,
)
from backend.db.user_operations import get_user_by_id
from backend.errors.error import (
    AlchemyToPydanticErr,
    PydanticToAlchemyErr,
    TaskNotFound,
    UserNotFound,
)
from backend.logger.logger import custom_logger
from backend.models.model import PyTask as PyTask
from backend.db.migrations import User, Task


def add_task(task_to_add: PyTask, user_id: str, session: Session) -> None:
    """
    accepts Pydantic task and user_id of the owner of the task and adds it to the database, returns None for success
    raises PydanticToAlchemyErr,UserNotFound,SQLAlchemyError
    """
    try:
        sql_alchemy_task_to_add = new_task_pydantic_to_alchemy(task_to_add, user_id)
        session.add(sql_alchemy_task_to_add)
        session.commit()

    except AlchemyToPydanticErr as e:
        custom_logger.error("Error in converting model from alchemy to pydantic", e)
        raise e

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error in converting model from pydantic to alchemy", e)
        raise e

    except UserNotFound as e:
        custom_logger.error("The user whose task needs to be added, doesnt exist : ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.info(
            "Error while adding a task during sqlalchemy operation : ", e
        )
        raise e


def get_all_task(user_id: str, session: Session) -> list[PyTask] | None:
    """
    gets all tasks for a given userid, else returns error
    returns AlchemyToPydanticErr,UserNotFound,SQLAlchemyError,Exception based on operations
    """
    try:
        user_by_id = get_user_by_id(user_id)
        all_tasks_stmt = select(Task).where(
            and_(Task.user_id == user_id, Task.is_deleted == False)
        )
        rows = session.execute(all_tasks_stmt)
        pydantic_task_list: list[PyTask] = []
        for obj in rows.scalars().all():
            pyd_obj = task_alchemy_to_pydantic(obj)
            pydantic_task_list.append(pyd_obj)
        custom_logger.info(
            f"TASK LIST RETURNED :  {pydantic_task_list}",
        )
        return pydantic_task_list

    except AlchemyToPydanticErr as e:
        custom_logger.error("Error in converting model from alchemy to pydantic", e)
        raise e

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error in converting model from pydantic to alchemy", e)
        raise e

    except UserNotFound as e:
        custom_logger.error("The user whose task needs to be added, doesnt exist : ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.info(
            "Error while adding a task during sqlalchemy operation : ", e
        )
        raise e


def delete_task(task_id: str, session: Session) -> None:
    """
    deletes a task by setting the is_deleted flag to true for it,
    Errors = TaskNotFound,AlchemyToPydanticErr,SQLAlchemyError,Exception
    """
    try:
        task = (
            session.query(Task)
            .filter(and_(Task.task_id == task_id, Task.is_deleted == False))
            .first()
        )

        if task:
            task.is_deleted = True
            session.commit()
        else:
            raise TaskNotFound

    except TaskNotFound as e:
        custom_logger.error("Task not found in the database while deleting ", e)
        raise e

    except AlchemyToPydanticErr as e:
        custom_logger.error("Error in converting model from alchemy to pydantic", e)
        raise e

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error in converting model from pydantic to alchemy", e)
        raise e

    except UserNotFound as e:
        custom_logger.error("The user whose task needs to be added, doesnt exist : ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.info(
            "Error while adding a task during sqlalchemy operation : ", e
        )
        raise e


def update_task(
    user_id: str, old_task_id: str, new_task: PyTask, session: Session
) -> None:
    """
    Takes in old_task_id and a new pyTask object and updates it in database
    returns none if success else returns error
    Errors = TaskNotFound,SQLAlchemyError,Exception
    """
    try:
        delete_task(old_task_id, session)
        add_task(new_task, user_id, session)

    except TaskNotFound as e:
        custom_logger.error("Task not found in the database while deleting ", e)
        raise e

    except AlchemyToPydanticErr as e:
        custom_logger.error("Error in converting model from alchemy to pydantic", e)
        raise e

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error in converting model from pydantic to alchemy", e)
        raise e

    except UserNotFound as e:
        custom_logger.error("The user whose task needs to be added, doesnt exist : ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.info(
            "Error while adding a task during sqlalchemy operation : ", e
        )
        raise e


def get_task_by_id(task_id: str, session: Session) -> PyTask | Exception:
    """
    Gets a task by id
    return task model if exists, or error if user not found
    Errors = TaskNotFound,SQLAlchemyError,Exception
    """
    try:
        stmt = (
            select(Task)
            .where(and_(Task.task_id == task_id, Task.is_deleted == False))
            .limit(1)
        )
        result = session.execute(stmt)
        task = result.scalars().first()
        if task:
            return task_alchemy_to_pydantic(task)
        else:
            raise TaskNotFound

    except TaskNotFound as e:
        custom_logger.error("Task not found in the database while deleting ", e)
        raise e

    except AlchemyToPydanticErr as e:
        custom_logger.error("Error in converting model from alchemy to pydantic", e)
        raise e

    except PydanticToAlchemyErr as e:
        custom_logger.error("Error in converting model from pydantic to alchemy", e)
        raise e

    except UserNotFound as e:
        custom_logger.error("The user whose task needs to be added, doesnt exist : ", e)
        raise e

    except SQLAlchemyError as e:
        custom_logger.info(
            "Error while adding a task during sqlalchemy operation : ", e
        )
        raise e
