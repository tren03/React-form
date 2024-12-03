import sqlite3
from sqlite3.dbapi2 import Error
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# returns db conn object or None
def get_db_conn():
    conn = None
    try:
        conn = sqlite3.connect("./database/tododb.db")
    except sqlite3.Error:
        print(f"error connect to database - {Error}")
    finally:
        return conn


class Task(BaseModel):
    taskId: int
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
