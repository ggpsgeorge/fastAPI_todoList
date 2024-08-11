from sqlalchemy import String, Integer, Column, DateTime
from sqlalchemy.sql import func
from app.api.db.database import Base
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String(256), nullable=False, index=True)
    description = Column(String(2048), index=True)
    created = Column(DateTime(timezone=False), nullable=False, default=datetime.now())
