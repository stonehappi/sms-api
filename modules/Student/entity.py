
from sqlalchemy import Column, Integer, String
from core.database import Base

from core.entity import Entity

class Student(Entity, Base ):
    __tablename__= "Student"
    name = Column(String)
    address = Column(String)
    age = Column(Integer)
