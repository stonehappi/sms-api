from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.entity import Entity
from core.database import Base


class Company(Entity, Base):
    __tablename__ = "Company"
    #id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    Address = Column(String)

    positions = relationship("Position", back_populates= "company")