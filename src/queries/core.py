import asyncio
from sqlalchemy import text
from src.database import engine



async def version_query():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"=== {res.scalar_one_or_none()} ===")


asyncio.run(version_query())