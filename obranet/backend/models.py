import reflex as rx 
import sqlmodel
import sqlalchemy
import datetime
# from datetime import datetime
from sqlmodel import Field


# class Registrado(rx.Model, table=True):
#     name:str
#     email: str = Field(sa_column=sqlalchemy.Column("email", sqlalchemy.String, unique=True))
#     phone:str
#     location:str 
#     service:str
#     description:str
    

#     created_ts: datetime.datetime = sqlmodel.Field(
#         default=None,
#         sa_column=sqlalchemy.Column(
#             "created_ts",
#             sqlalchemy.DateTime(timezone=True),
#             server_default=sqlalchemy.func.now(),
#         ),
#     )
#     update_ts: datetime.datetime = sqlmodel.Field(
#         default=None,
#         sa_column=sqlalchemy.Column(
#             "update_ts",
#             sqlalchemy.DateTime(timezone=True),
#             server_default=sqlalchemy.func.now(),
#             onupdate=sqlalchemy.func.now(),
#         ),
#     )


# class Contact(rx.Model, table=True):
#     name: str
#     email: str
#     message: str
#     created_at: datetime.datetime = sqlmodel.Field(
#         default=None,
#         sa_column=sqlalchemy.Column(
#             "created_at",
#             sqlalchemy.DateTime(timezone=True),
#             server_default=sqlalchemy.func.now(),
#         ),
#     )

#     def dict(self, *args, **kwargs) -> dict:
#         d = super().dict(*args, **kwargs)
#         d["created_at"] = self.created_at.replace(
#             microsecond=0
#         ).isoformat()
#         return d
    