import asyncio
from db import engine, Base
from models.reminder import Reminder

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_all())