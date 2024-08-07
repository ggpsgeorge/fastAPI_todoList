from sqlalchemy.orm import Session

from app.api.models import task_model
from app.api.schemas import task_schema

def create_task(db: Session, task: task_schema.TaskCreate):
    db_task = task_model.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task