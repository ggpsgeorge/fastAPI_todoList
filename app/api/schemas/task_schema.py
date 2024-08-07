from pydantic import BaseModel
from typing import Union

class TaskBase(BaseModel):
    title: str
    description: Union[str, None] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class config:
        orm_mode: True