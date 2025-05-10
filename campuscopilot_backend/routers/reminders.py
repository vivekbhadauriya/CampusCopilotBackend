from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db import SessionLocal
from models.reminder import Reminder, ReminderCreate, ReminderOut

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=ReminderOut)
async def create_reminder(reminder: ReminderCreate, db: AsyncSession = Depends(get_db)):
    db_reminder = Reminder(
        title=reminder.title,
        description=reminder.description,
        due_time=reminder.due_time,
        priority=reminder.priority,
        category=reminder.category
    )
    db.add(db_reminder)
    await db.commit()
    await db.refresh(db_reminder)
    return db_reminder

@router.get("/", response_model=list[ReminderOut])
async def list_reminders(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reminder))
    return result.scalars().all()

@router.delete("/{reminder_id}", response_model=dict)
async def delete_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reminder).where(Reminder.id == reminder_id))
    reminder = result.scalar_one_or_none()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    await db.delete(reminder)
    await db.commit()
    return {"ok": True}

@router.patch("/{reminder_id}", response_model=ReminderOut)
async def toggle_reminder(reminder_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Reminder).where(Reminder.id == reminder_id))
    reminder = result.scalar_one_or_none()
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    reminder.completed = not reminder.completed
    await db.commit()
    await db.refresh(reminder)
    return reminder