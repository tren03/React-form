from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    task_title: str
    task_description: str
    task_category: str


class LoginDetails(BaseModel):
    email: str
    password: str


class User(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: str
    phone: str
    password: str
