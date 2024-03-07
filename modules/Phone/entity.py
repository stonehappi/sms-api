from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Phone(Entity, Base):
    __tablename__="phone"
    number = Column(String)
    name  = Column(String)
    contactid = Column(Integer)