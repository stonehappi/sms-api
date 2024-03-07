from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class position(Entity, Base):
    __tablename__="position"
    name  = Column(String)
    Address = Column(Integer)