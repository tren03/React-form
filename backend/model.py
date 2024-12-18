from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    taskId: Optional[int] = None
    taskTitle: str
    taskDescription: str
    taskCategory: str


class User(BaseModel):
    f_name: str
    l_name: str
    user_name: str
    email: str
    phone: str
    password: str
