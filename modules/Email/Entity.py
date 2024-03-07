from sqlalchemy import Column, Integer, String
from core.database import Base

from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "Email"
    Mail = Column(String)
    Name = Column(String)
    ContactId = Column(Integer)

    