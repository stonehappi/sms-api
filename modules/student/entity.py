from sqlalchemy import Column, Integer, String

from core.entity import Entity
from core.database import Base


class Student(Entity, Base):
    __tablename__ = "Student"
    name = Column(String, unique=True)
    address = Column(String)
    age = Column(Integer)