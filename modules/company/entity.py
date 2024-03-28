from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from core.database import Base
from core.entity import Entity
from sqlalchemy.orm import relationship


class Company(Entity, Base):
    __tablename__ = "company"
    name = Column(String, name="Name", index=True, unique=True, nullable=False)
    address = Column(Integer, name="Address")

    positions = relationship("Position", back_populates="company")

