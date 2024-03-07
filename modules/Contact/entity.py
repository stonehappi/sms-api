

from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "contact"
    firstname = Column(String, index=True)
    lastname = Column(String)
    positionid = Column(Integer)