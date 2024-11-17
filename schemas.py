from pydantic import BaseModel
from typing import List, Optional


class TaskCreate(BaseModel):
    title: str
    description: str


class Task(TaskCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    full_name: str
    password: str


class User(BaseModel):
    id: int
    email: str
    full_name: str
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
