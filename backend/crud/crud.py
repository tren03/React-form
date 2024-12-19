from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body
from sqlalchemy.exc import SQLAlchemyError
from backend.errors.error import TaskNotFound, UserNotFound
from backend.models.model import Task
from backend.db.db_connection import get_db_conn, get_session
from backend.db.task_operations import (
    add_task as add_task_to_db,
    get_all_task as get_all_tasks_from_db,
    delete_task as delete_task_from_db,
)

from typing import Annotated

router = APIRouter()


@router.post("/add_task")
async def add_task(task: Task, user_id: Annotated[str, Body()]):
    """
    Takes a Task and userid and adds it to the database
    """
    stat = add_task_to_db(task, user_id, get_session())

    if isinstance(stat, UserNotFound):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User to add task not found: {str(stat)}",
        )

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error while adding task: {str(stat)}",
        )

    # addition successful
    stat = get_all_tasks_from_db(user_id, get_session())

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting tasks from database: {str(stat)}",
        )

    return {"task_list": stat}


# for now we take user_id, but after jwt, we get user_id from there
@router.post("/delete_task")
async def delete_task(user_id: Annotated[str, Body()], task_id: Annotated[str, Body()]):
    """
    Takes a task_id and sets the delete flag to true
    """
    stat = delete_task_from_db(task_id, get_session())

    if isinstance(stat, TaskNotFound):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task to delete not found",
        )

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error while adding task: {str(stat)}",
        )

    # deletion successful
    stat = get_all_tasks_from_db(user_id, get_session())

    if isinstance(stat, UserNotFound):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error while getting tasks from databse : {str(stat)}",
        )

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting tasks from database: {str(stat)}",
        )

    return {"task_list": stat}
