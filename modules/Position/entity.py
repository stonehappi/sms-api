

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship 
from core.database import Base
from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "position"
    name = Column(String, index=True, name="Name")
    companyid = Column(Integer, ForeignKey("company.id"), name="CompanyId")
    
    company = relationship("Company", back_populates="positions")