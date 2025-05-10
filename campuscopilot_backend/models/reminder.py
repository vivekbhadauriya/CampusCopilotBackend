from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from db import Base
import enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class CategoryEnum(str, enum.Enum):
    academic = "academic"
    meeting = "meeting"
    errands = "errands"
    personal = "personal"

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_time = Column(DateTime, nullable=False)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.medium)
    category = Column(Enum(CategoryEnum), default=CategoryEnum.personal)
    completed = Column(Boolean, default=False)

# Pydantic models for request/response
class ReminderBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_time: datetime
    priority: PriorityEnum = PriorityEnum.medium
    category: CategoryEnum = CategoryEnum.personal

class ReminderCreate(ReminderBase):
    pass

class ReminderOut(ReminderBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True