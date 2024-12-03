import sqlite3
from sqlite3.dbapi2 import Error
from typing_extensions import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# returns db conn object or None
def get_db_conn():
    conn = None
    try:
        conn = sqlite3.connect("tododb.db")
    except sqlite3.Error:
        print(f"error connect to database - {Error}")
    finally:
        return conn


class Task(BaseModel):
    taskId: Optional[int] = None
    taskTitle: str
    taskDescription: str
    taskCategory: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your React app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/get_tasks")
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


@app.post("/add_task", response_model=list[Task])
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
@app.post("/delete_task")
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
