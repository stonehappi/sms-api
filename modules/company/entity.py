from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class company(Entity, Base):
    __tablename__="company"
    Name = Column(String)
    Address = Column(Integer)