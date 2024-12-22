from typing import Optional

from pydantic import BaseModel


class TokenDto(BaseModel):
    access_token: str


class TaskDto(BaseModel):
    task_id: Optional[str] = None
    task_title: str
    task_description: str
    task_category: str
    # user_id: str


class LoginDetailsDto(BaseModel):
    email: str
    password: str


class UserSignInDto(BaseModel):
    user_id: Optional[str] = None
    first_name: str
    last_name: str
    user_name: str
    email: str
    phone: str
    password: str


class UserDto(BaseModel):
    user_id: Optional[str] = None
    first_name: str
    last_name: str
    user_name: str
    email: str
    phone: str
