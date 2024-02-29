from sqlalchemy import Column, Integer, String, DateTime
from core.database import Base
from core.entity import Entity

class Position(Entity, Base):
    __tablename__="position"
    positonname = Column(String, index=True)
    salary = Column(Integer)
    Sex = Column(String)
    Age = Column(Integer)
    email = Column(String)
    Address = Column(String)
    timeWork = Column(DateTime)
    Fullname = Column(String)
