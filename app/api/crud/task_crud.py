from sqlalchemy.orm import Session

from app.api.models import task_model
from app.api.schemas import task_schema

def create_task(db: Session, task: task_schema.TaskCreate):
    db_task = task_model.Task(**task.model_dump())    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_task(db: Session, task_id: int):
    db_task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    return db_task