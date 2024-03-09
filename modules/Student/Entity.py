from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from core.database import Base

from core.entity import Entity


class Student(Entity, Base):
    __tablename__ = "Student"
    name = Column(String)
    address = Column(String)
    Age = Column(int)
    

    