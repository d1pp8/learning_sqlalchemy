from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

workers_tabel = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)

