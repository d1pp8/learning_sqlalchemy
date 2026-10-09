from src.database import Base
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column


metadata_obj = MetaData()


class Workers(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]




# workers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("username", String)
# )

