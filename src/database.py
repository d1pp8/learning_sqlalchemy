import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import URL, text
from config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNCPG,
    echo=True,
    # pool_size=8,
    # max_overflow=16,
)

async def version_query():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"=== {res.scalar_one_or_none()} ===")


asyncio.run(version_query())