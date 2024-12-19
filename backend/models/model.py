from pydantic import BaseModel
from typing import Optional


class UserID(BaseModel):
    user_id: str


class JWTInfo(BaseModel):
    user_id: str
    email: str


# By changing the schema we break all crud operations done before sqlalchemy
class PyTask(BaseModel):
    task_title: str
    task_description: str
    task_category: str


class LoginDetails(BaseModel):
    email: str
    password: str


class PyUser(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: str
    phone: str
    password: str
