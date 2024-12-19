from sqlalchemy import and_, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import task_alchemy_to_pydantic, task_pydantic_to_alchemy
from backend.db.user_operations import get_user_by_id
from backend.errors.error import (
    AlchemyToPydanticErr,
    PydanticToAlchemyErr,
    TaskNotFound,
    UserNotFound,
)
from backend.models.model import Task as PyTask
from backend.db.migrations import User, Task


def add_task(task_to_add: PyTask, user_id: str, session: Session) -> None | Exception:
    """
    accepts Pydantic task and user_id of the owner of the task and adds it to the database, returns None for success
    returns PydanticToAlchemyErr,UserNotFound,SQLAlchemyError,Exception based on operations
    """
    try:
        user_by_id = get_user_by_id(user_id)

        # could be a Usernotfound or sqlalchemy to pydantic conversion
        if isinstance(user_by_id, Exception):
            raise user_by_id

        sql_alchemy_task_to_add = task_pydantic_to_alchemy(task_to_add, user_id)

        if isinstance(sql_alchemy_task_to_add, Exception):
            raise sql_alchemy_task_to_add

        session.add(sql_alchemy_task_to_add)
        session.commit()

    except PydanticToAlchemyErr as e:
        print("Error in converting model from pydantic to alchemy", e)

        return e
    except UserNotFound as e:
        print("The user whose task needs to be added, doesnt exist : ", e)
        return e

    except SQLAlchemyError as e:
        print("Error while adding a task during sqlalchemy operation : ", e)

    except Exception as e:
        print("General error while adding task :", e)
        return e


def get_all_task(user_id: str, session: Session) -> list[PyTask] | Exception:
    """
    gets all tasks for a given userid, else returns error
    returns AlchemyToPydanticErr,UserNotFound,SQLAlchemyError,Exception based on operations
    """
    try:
        user_by_id = get_user_by_id(user_id)

        # could be a Usernotfound or sqlalchemy to pydantic conversion
        if isinstance(user_by_id, Exception):
            raise user_by_id

        all_tasks_stmt = select(Task).where(
            and_(Task.user_id == user_id, Task.is_deleted == False)
        )

        rows = session.execute(all_tasks_stmt)
        pydantic_task_list: list[PyTask] = []
        for obj in rows.scalars().all():
            pyd_obj = task_alchemy_to_pydantic(obj)

            if isinstance(pyd_obj, Exception):
                raise pyd_obj

            pydantic_task_list.append(pyd_obj)
        print("TASK LIST RETURNED : ", pydantic_task_list)
        return pydantic_task_list

    except AlchemyToPydanticErr as e:
        print("Error in converting model from alchemy to pydantic", e)
        return e

    except UserNotFound as e:
        print("The user whose task needs to be added, doesnt exist : ", e)
        return e

    except SQLAlchemyError as e:
        print("Errror in getting all tasks during sqlalchemy operation : ", e)
        return e

    except Exception as e:
        print("General error while getting all tasks :", e)
        return e


def delete_task(task_id: str, session: Session) -> None | Exception:
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
        print("Task not found in the database while deleting")
        return e

    except AlchemyToPydanticErr as e:
        print("Error in converting model from alchemy to pydantic", e)
        return e

    except SQLAlchemyError as e:
        print("Errror in getting all tasks during sqlalchemy operation : ", e)
        return e

    except Exception as e:
        print("General error while getting all tasks :", e)
        return e


def update_task(
    user_id: str, old_task_id: str, new_task: PyTask, session: Session
) -> None | Exception:
    """
    Taked in old_task_id and a new pyTask object and updates it in database
    returns none if success else returns error
    Errors = TaskNotFound,SQLAlchemyError,Exception
    """
    try:
        delete_task_flag = delete_task(old_task_id, session)
        if isinstance(delete_task_flag, Exception):
            raise delete_task_flag

        add_updated_task = add_task(new_task, user_id, session)
        if isinstance(add_updated_task, Exception):
            raise add_updated_task

    except TaskNotFound as e:
        print("Task not found in the database while deleting")
        return e

    except AlchemyToPydanticErr as e:
        print("Error in converting model from alchemy to pydantic", e)
        return e

    except PydanticToAlchemyErr as e:
        print("Error in converting model from pydantic to alchemy", e)
        return e

    except UserNotFound as e:
        print("The user whose task needs to be added, doesnt exist : ", e)
        return e

    except SQLAlchemyError as e:
        print("Errror in getting all tasks during sqlalchemy operation : ", e)
        return e

    except Exception as e:
        print("General error while getting all tasks :", e)
        return e


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
        print(f"Task not found in database", e)
        return e

    except SQLAlchemyError as e:
        print(
            "Error in getting task by id from database during sqlalchemy operation", e
        )
        return e

    except Exception as e:
        print(f"Something went wrong while getting task by id from database", e)
        return e
