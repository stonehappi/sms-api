
from sqlalchemy import Column, String
from core.database import Base
from core.entity import Entity


class Company(Entity, Base):
    __tablename__ = "company"
    name = Column(String)
    address = Column(String)