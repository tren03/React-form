from typing import Annotated

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body

from backend.db.db_connection import get_db_conn, get_session
from backend.db.task_operations import add_task as add_task_to_db
from backend.db.task_operations import delete_task as delete_task_from_db
from backend.db.task_operations import get_all_task as get_all_tasks_from_db
from backend.db.task_operations import update_task as update_task_to_db
from backend.errors.error import CustomError, TaskNotFound, UserNotFound
from backend.logger.logger import custom_logger
from backend.models.dto import TaskDto, UserIdDto

router = APIRouter()


@router.post("/add_task")
async def add_task(task: TaskDto, user_id: Annotated[str, Body()]):
    """
    Takes a Task and userid and adds it to the database
    """
    try:
        add_task_to_db(task, user_id, get_session())
        all_tasks = get_all_tasks_from_db(user_id, get_session())
        custom_logger.info(
            f"list returned after addition for user {user_id} = {all_tasks} "
        )
        return {"task_list": all_tasks}

    except UserNotFound as e:
        custom_logger.info("User not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User to add task not found",
        )

    except CustomError as e:
        custom_logger.info("Err during adding task ", e.message())
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error while adding task",
        )


# for now we take user_id, but after jwt, we get user_id from there
@router.post("/delete_task")
async def delete_task(user_id: Annotated[str, Body()], task_id: Annotated[str, Body()]):
    """
    Takes a task_id and sets the delete flag to true
    """
    try:

        delete_task_from_db(task_id, get_session())
        all_tasks = get_all_tasks_from_db(user_id, get_session())
        custom_logger.info(f"list returned after deleting task = {all_tasks} ")
        return {"task_list": all_tasks}

    except TaskNotFound as e:
        custom_logger.error("task to delete not found ", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task to delete not found",
        )

    except UserNotFound as e:
        custom_logger.error("User whose task needs to be deleted not found", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task to delete not found",
        )

    except CustomError as e:
        custom_logger.error("err during deletion of task ", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"err deleting task",
        )


@router.post("/update_task")
async def update_task(
    user_id: Annotated[str, Body()],
    old_task_id: Annotated[str, Body()],
    new_task: TaskDto,
):
    """
    Takes a user_id, old_task_id, and a new_task  ,sets the delete flag to true on old_task and adds new task and returns all tasks
    """
    try:

        update_task_to_db(user_id, old_task_id, new_task, get_session())
        all_tasks = get_all_tasks_from_db(user_id, get_session())
        custom_logger.info(
            f"list returned after updating task for user {user_id} = {all_tasks} "
        )
        return {"task_list": all_tasks}

    except TaskNotFound as e:
        custom_logger.error("task to delete not found ", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task to delete not found",
        )

    except UserNotFound as e:
        custom_logger.error("User whose task needs to be deleted not found", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task to delete not found",
        )

    except CustomError as e:
        custom_logger.error("err during deletion of task ", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"err deleting task",
        )


@router.post("/get_all_tasks")
async def get_all_tasks(UID: UserIdDto):
    """
    Given a user_id, returns all tasks of that user
    """
    try:
        all_tasks = get_all_tasks_from_db(UID.user_id, get_session())
        custom_logger.info(f"list returned for user {UID.user_id} = {all_tasks} ")
        return {"task_list": all_tasks}

    except UserNotFound as e:
        custom_logger.error("User whose task needs to be deleted not found", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user not found",
        )

    except CustomError as e:
        custom_logger.error("err during deletion of task ", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"err gettinga all tasks task",
        )
