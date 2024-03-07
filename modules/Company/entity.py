
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship 
from core.database import Base
from core.entity import Entity


class Company(Entity, Base):
    __tablename__ = "company"
    name = Column(String, index=True, name="Company Name")
    address = Column(String)
    
    positions = relationship("Position", back_populates="company")