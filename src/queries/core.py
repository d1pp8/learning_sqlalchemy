from sqlalchemy import insert, text

from src.database import engine
from src.models import metadata_obj, workers_table



async def version_query():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"=== {res.scalar_one_or_none()} ===")


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)


async def insert_data():
    async with engine.connect() as conn:
        # stmt = """
        # INSERT INTO workers (username) VALUES
        # ('AO Bobr'),
        # ('OOO Volk');
        # """

        stmt = insert(workers_table).values(
            [
                {"username": "Ivan"},
                {"username": "Vasya"}
            ]
        )
        await conn.execute(stmt)
        await conn.commit()