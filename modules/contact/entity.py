from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class contact(Entity, Base):
    __tablename__="contact"
    Firstname  = Column(String)
    LatName = Column(Integer)
    PositionId = Column(Integer)