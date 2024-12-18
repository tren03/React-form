from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.db.conversions import task_alchemy_to_pydantic, task_pydantic_to_alchemy
from backend.errors.error import (
    AlchemyToPydanticErr,
    PydanticToAlchemyErr,
    TaskAdditionError,
    UserNotFound,
)
from backend.models.model import Task as PyTask
from backend.db.migrations import User, Task


def add_task(task_to_add: PyTask, user_id: str, session: Session) -> None | Exception:
    """
    accepts Pydantic task and user_id of the owner of the task and adds it to the database
    """
    try:
        if not session.query(User).filter(User.user_id == user_id).first():
            raise UserNotFound()
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
    """
    try:
        if not session.query(User).filter(User.user_id == user_id).first():
            raise UserNotFound()
        all_tasks_stmt = select(Task).where(Task.user_id == user_id)
        rows = session.execute(all_tasks_stmt)
        pydantic_task_list: list[PyTask] = []
        for obj in rows.scalars().all():
            pyd_obj = task_alchemy_to_pydantic(obj)

            if isinstance(pyd_obj, Exception):
                raise pyd_obj

            pydantic_task_list.append(pyd_obj)
        return pydantic_task_list

    except AlchemyToPydanticErr as e:
        print("Error in converting model from alchemy to pydantic", e)
        return e

    except SQLAlchemyError as e:
        print("Errror in getting all tasks during sqlalchemy operation : ", e)
        return e

    except UserNotFound as e:
        print("The user whose task needs to be added, doesnt exist : ", e)
        return e

    except Exception as e:
        print("General error while getting all tasks :", e)
        return e


# def add_user(user_to_add: PyUser, session: Session) -> None | Exception:
#     """
#     Adds a user to the "user" table and session
#     Accepts a pydantic user model and adds in to the database by converting to sqlalchemy model
#
#     return:
#     None - success
#     Exception - any error during addition
#
#     """
#     try:
#         print(uuid.uuid4())
#         if session.query(User).filter(User.email == user_to_add.email).first():
#             # we have a existing user
#             raise DuplicateUserError
#
#         sql_alchemy_user_to_add = user_pydantic_to_alchemy(user_to_add)
#         session.add(sql_alchemy_user_to_add)
#         session.commit()
#
#     except DuplicateUserError as e:
#         print(f"DuplicateUserError {e}")
#         return e
#
#     except SQLAlchemyError as e:
#         print(f"exception during user creation {e}")
#         return e
#
#     except Exception as e:
#         print(f"something went wrong in addition of user during sign in ", e)
#         return e
#
