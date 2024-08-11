from pydantic import BaseModel
from typing import Union
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Union[str, None] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created: datetime 

    class config:
        orm_mode: True