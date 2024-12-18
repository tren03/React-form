from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body
from sqlalchemy.exc import SQLAlchemyError
from backend.errors.error import UserNotFound
from backend.models.model import Task
from backend.db.db_connection import get_db_conn, get_session
from backend.db.task_operations import add_task as add_task_to_db, get_all_task
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error while adding task: {str(stat)}",
        )

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error while adding task: {str(stat)}",
        )

    # addition successful
    stat = get_all_task(user_id, get_session())

    if isinstance(stat, UserNotFound):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error while adding task: {str(stat)}",
        )

    if isinstance(stat, Exception):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error while adding task: {str(stat)}",
        )

    return {"task_list": stat}
