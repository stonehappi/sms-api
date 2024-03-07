from sqlalchemy import Column, Integer, String
from core.database import Base

from core.entity import Entity


class Phone(Entity, Base):
    __tablename__ = "Phone"
    Number = Column(Integer)
    Name = Column(String)
    ContactId = Column(Integer)

    