from sqlalchemy import Column, Integer, String
from core.database import Base

from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "Contact"
    FirstName = Column(String)
    LastName = Column(String)
    PositionId = Column(Integer)

    