from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.schemas import task_schema
from app.api.models import task_model
from app.api.crud import task_crud
from app.api.db.database import SessionLocal, engine

task_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks/", response_model=task_schema.Task)
async def create_task(task: task_schema.TaskCreate, db: Session = Depends(get_db)):
    db_task = task_crud.create_task(db, task)
    return db_task    

@router.get("/tasks/{task_id}")
async def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_crud.read_task(db, task_id)
    return db_task