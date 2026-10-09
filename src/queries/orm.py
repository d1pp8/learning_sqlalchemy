from src.database import engine, async_session
from src.models import metadata_obj, Workers


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)


async def insert_data():
    worker_volk = Workers(username="Volk")
    worker_ivan = Workers(username="Ivan")

    async with async_session() as session:
        session.add_all([worker_volk, worker_ivan])
        await session.commit()