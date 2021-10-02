from sqlalchemy import Column, String, Integer,Float,DateTime,Text
from sqlalchemy.schema import ForeignKey
from db import engine
from sqlalchemy.orm import sessionmaker, relationship
import datetime

from sqlalchemy import Column, Table
from db import meta, engine

datos_falsos = Table(
    "datos_falsos",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "name",
        String(255),
    ),
    Column("email", String(255)),
)

meta.create_all(engine)
