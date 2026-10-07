from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNCPG,
    echo=True,
    # pool_size=8,
    # max_overflow=16,
)


