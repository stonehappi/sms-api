
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Student(Entity, Base):
    __tablename__ = "student"
    name = Column(String, name="Name", index=True)
    address = Column(String, name="Address")
    age = Column(Integer, name="Age")