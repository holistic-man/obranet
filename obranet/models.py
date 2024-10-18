import reflex as rx 
import sqlmodel
import sqlalchemy
import datetime
# from datetime import datetime
from sqlmodel import Field
from typing import List, Optional

# from datetime import datetime, timezone


class Registrado(rx.Model, table=True):
    name:str
    email: str = Field(sa_column=sqlalchemy.Column("email", sqlalchemy.String, unique=True))
    phone:str
    location:str 
    service:str
    description:str
    photo: Optional[str] = None
    

    created_ts: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "created_ts",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    update_ts: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "update_ts",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
            onupdate=sqlalchemy.func.now(),
        ),
    )

class Contact(rx.Model, table=True):
    name: str
    email: str
    message: str
    created_at: datetime.datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "created_at",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )
    
    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["created_at"] = self.created_at.replace(
            microsecond=0
        ).isoformat()
        return d
    

# class User(rx.Model, table=True):
    
#     email: str = Field(sa_column=sqlalchemy.Column("email", sqlalchemy.String, unique=True))

#     created_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     )

#     update_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'onupdate': sqlalchemy.func.now(),
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     )    

# class UserComplete(rx.Model, table=True):
#     name: str
#     email: str = Field(sa_column=sqlalchemy.Column("email", sqlalchemy.String, unique=True))
#     phone: str
#     service: str
#     description: str

#     created_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     )

#     update_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'onupdate': sqlalchemy.func.now(),
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     )   

# class Profile(rx.Model, table=True):
#     name: str
#     phone: str
#     region: str
#     commune: str
#     service: str
#     description: str
#     created_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     )

#     update_ts: datetime = Field(
#         default_factory=datetime.now(),
#         sa_type=sqlalchemy.DateTime(timezone=True),
#         sa_column_kwargs={
#             'onupdate': sqlalchemy.func.now(),
#             'server_default':sqlalchemy.func.now()
#         },
#         nullable=False
#     ) 