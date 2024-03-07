from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class email(Entity, Base):
    __tablename__="email"
    Mail = Column(String)
    Name = Column(String)
    Contactid= Column(Integer)