from sqlalchemy import String, Integer, Column
from app.api.db.database import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String(256), nullable=False, index=True)
    description = Column(String(2048), index=True)
    # timeStamp = Column(DateTime, index=True)