from fastapi import APIRouter
from backend.model import Task
from backend.db import get_db_conn
import sqlite3

router = APIRouter()


@router.get("/get_tasks")
async def get_tasks():

    data_to_send = []

    conn = get_db_conn()
    if not conn:
        return {"error getting data from db"}

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    for row in rows:
        task = Task(
            taskId=row[0], taskTitle=row[1], taskDescription=row[2], taskCategory=row[3]
        )
        data_to_send.append(task)

    conn.close()

    return data_to_send


@router.post("/add_task", response_model=list[Task])
async def add_task(task: Task):
    conn = get_db_conn()
    if not conn:
        return {"error": "Error getting data from db"}

    try:
        cursor = conn.cursor()

        # Insert the task into the database (taskId is handled by SQLite auto-increment)
        cursor.execute(
            """
            INSERT INTO tasks (taskTitle, taskDescription, taskCategory)
            VALUES (?, ?, ?)
            """,
            (task.taskTitle, task.taskDescription, task.taskCategory),
        )

        # Commit the changes
        conn.commit()

        # Get the updated list of tasks
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        # Create a list of Task objects from the rows
        tasks_list = [
            Task(
                taskId=row[0],
                taskTitle=row[1],
                taskDescription=row[2],
                taskCategory=row[3],
            )
            for row in rows
        ]

        return tasks_list  # Return the updated list of tasks

    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}

    finally:
        conn.close()


# if we need to send id as a json payload, then we have to make a pydantic model, otherwise passed as query param
@router.post("/delete_task")
async def delete_task(id: int):
    conn = get_db_conn()
    if not conn:
        return {"error": "Error getting data from db"}

    try:
        cursor = conn.cursor()

        # Delete the task from the database based on the provided taskId
        cursor.execute(
            """
            DELETE FROM tasks
            WHERE taskId = ?
            """,
            (id,),
        )

        # Commit the changes
        conn.commit()

        # Get the updated list of tasks after deletion
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        # Create a list of Task objects from the rows
        tasks_list = [
            Task(
                taskId=row[0],
                taskTitle=row[1],
                taskDescription=row[2],
                taskCategory=row[3],
            )
            for row in rows
        ]

        return tasks_list  # Return the updated list of tasks

    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}

    finally:
        conn.close()


@router.post("/update_task")
async def update_task(id: int, task: Task):
    conn = get_db_conn()
    if not conn:
        return {"error": "Error getting data from db"}

    try:
        cursor = conn.cursor()

        # Update the task in the database based on the provided taskId
        cursor.execute(
            """
            UPDATE tasks
            SET taskTitle = ?, taskDescription = ?, taskCategory = ?
            WHERE taskId = ?
            """,
            (task.taskTitle, task.taskDescription, task.taskCategory, id),
        )

        # Commit the changes
        conn.commit()

        # Get the updated list of tasks after update
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        # Create a list of Task objects from the rows
        tasks_list = [
            Task(
                taskId=row[0],
                taskTitle=row[1],
                taskDescription=row[2],
                taskCategory=row[3],
            )
            for row in rows
        ]

        return tasks_list  # Return the updated list of tasks

    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}

    finally:
        conn.close()
