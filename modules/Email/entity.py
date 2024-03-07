

from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "email"
    mail = Column(String, index=True)
    name = Column(String)
    contactid = Column(Integer)