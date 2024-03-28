from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base
from core.entity import Entity


class Company(Entity, Base):
    __tablename__ = "company"
    name = Column(String)
    address = Column(String)

    positions= relationship("Position", back_populates="company")