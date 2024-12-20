from typing import Annotated

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Body

from backend.conversions.conversion_interface import IConversion
from backend.conversions.sqlite_conversions import SqliteConversion
from backend.db.db_connection import get_session
from backend.errors.error import CustomError, TaskNotFound, UserNotFound
from backend.logger.logger import custom_logger
from backend.models.dto import TaskDto, UserIdDto
from backend.models.entitiy import TaskEntity, UserEntity
from backend.repo.repo_interface import IRepo
from backend.repo.sqlite_repo import SqliteRepo

router = APIRouter()
converter: IConversion = SqliteConversion()
repo: IRepo = SqliteRepo(converter, get_session())


@router.post("/add_task")
async def add_task(task: TaskDto, user_id: Annotated[str, Body()]):
    """
    Takes a Task and userid and adds it to the database
    """
    try:
        task_entity = TaskEntity.task_dto_to_entity(task)
        repo.add_task(task_entity)
        all_task_entities = repo.get_all_tasks_of_user(user_id)
        all_task_dto = []
        for task_entity in all_task_entities:
            all_task_dto.append(TaskEntity.task_entity_to_dto(task_entity))

        custom_logger.info(
            f"list returned after addition for user {user_id} = {all_task_dto} "
        )
        return {"task_list": all_task_dto}

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

        repo.delete_task_by_id(task_id)
        all_task_entities = repo.get_all_tasks_of_user(user_id)
        all_task_dto = []
        for task_entity in all_task_entities:
            all_task_dto.append(TaskEntity.task_entity_to_dto(task_entity))

        custom_logger.info(f"list returned after deleting task = {all_task_dto} ")
        return {"task_list": all_task_dto}

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

        new_task_entity = TaskEntity.task_dto_to_entity(new_task)
        repo.update_task_by_id(old_task_id, new_task_entity)
        all_task_entities = repo.get_all_tasks_of_user(user_id)
        all_task_dto = []
        for task_entity in all_task_entities:
            all_task_dto.append(TaskEntity.task_entity_to_dto(task_entity))
        custom_logger.info(
            f"list returned after updating task for user {user_id} = {all_task_dto} "
        )
        return {"task_list": all_task_dto}

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
async def get_all_tasks(user_id: str):
    """
    Given a user_id, returns all tasks of that user (taskes user_id as parameter, not body)
    """
    try:
        custom_logger.info(f"user_id requested : {user_id}")
        all_task_entities = repo.get_all_tasks_of_user(user_id)
        all_task_dto = []
        for task_entity in all_task_entities:
            all_task_dto.append(TaskEntity.task_entity_to_dto(task_entity))

        custom_logger.info(
            f"list returned after addition for user {user_id} = {all_task_dto} "
        )
        return {"task_list": all_task_dto}

    except UserNotFound as e:
        custom_logger.error("User whose task needs to be deleted not found", e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user not found",
        )

    except TaskNotFound as e:
        return {"task_list": []}

    except CustomError as e:
        custom_logger.error("err during deletion of task ", e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"err gettinga all tasks task",
        )
