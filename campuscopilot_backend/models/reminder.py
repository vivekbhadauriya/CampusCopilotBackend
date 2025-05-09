from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from db import Base
import datetime

class Reminder(Base):
    __tablename__ = "reminders"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    due_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed = Column(Boolean, default=False)

class ReminderCreate(BaseModel):
    text: str
    due_time: datetime.datetime

class ReminderOut(BaseModel):
    id: int
    text: str
    due_time: datetime.datetime
    created_at: datetime.datetime
    completed: bool

    class Config:
        orm_mode = True