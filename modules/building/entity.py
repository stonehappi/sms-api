from sqlalchemy import Column, Integer, String, DateTime, Boolean
from core.database import Base
from core.entity import Entity


class Building(Entity, Base):
    __tablename__ = "building"
    name = Column(String)
    floor = Column(Integer)
    roos = Column(String)
    date = Column(DateTime)
    draft = Column(Boolean)
