from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class student(Entity, Base):
    __tablename__="student"
    name  = Column(String)
    address = Column(Integer)
    age = Column(Integer)
