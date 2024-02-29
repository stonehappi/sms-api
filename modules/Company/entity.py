from sqlalchemy import Column, Integer, String

from core.database import Base
from core.entity import Entity


class Company(Entity, Base):
    __tablename__ = "Company"
    Owner = Column(String)
    Founded = Column(Integer)
    Staff = Column(Integer)
    department = Column(Integer)
    location = Column(String)
    email = Column(String)
