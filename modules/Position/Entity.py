from sqlalchemy import Column, ForeignKey, Integer, String 
from core.database import Base
from sqlalchemy.orm import relationship
from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "Position"
    Name = Column(String)
    CompanyId = Column(Integer, ForeignKey("company.id"))
    address = Column(Integer, name="address")
    company = relationship("Company", back_populates="positions")
    contacts = relationship("Contact", back_populates="position")
    