from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth import get_current_user
from db import get_db
from models import Task
from schemas import TaskCreate, Task as TaskSchema, User

task_router = APIRouter()


@task_router.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = Task(title=task.title, description=task.description, user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@task_router.get("/tasks/", response_model=List[TaskSchema])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.user_id == current_user.id).offset(skip).limit(limit).all()
    return tasks
