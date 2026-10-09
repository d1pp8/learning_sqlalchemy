from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from src.config import settings



engine = create_async_engine(
    url=settings.DATABASE_URL_ASYNCPG,
    echo=True,
    # pool_size=8,
    # max_overflow=16,
)

async_session = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass

