from sqlalchemy import Column, String, Integer
from core.database import Base
from core.entity import Entity


class Department(Entity, Base):
    __tablename__ = "department"
    name = Column(String)
    short_name = Column(String)
    floor = Column(Integer)
    room = Column(Integer)

