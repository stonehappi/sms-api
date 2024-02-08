from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity

class Position(Entity, Base):
    __tablename__="position"
    positonname = Column(String, index=True)
    salary = Column(Integer)
    Sex = Column(String)
    Age = Column(Integer)

