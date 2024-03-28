from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "position"
    name = Column(String)
    
    
    companyid= Column(Integer, ForeignKey("company.id"))
    company= relationship("Company", back_populates="positions")
    
    contacts= relationship("Contact", back_populates="position")