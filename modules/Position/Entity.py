from sqlalchemy import Column, Integer, String, 
from core.database import Base
from sqlalchemy.orm import relationship
from core.entity import Entity


class Position(Entity, Base):
    __tablename__ = "Position"
    Name = Column(String)
    CompanyId = Column(Integer)
    address = Column(Integer, name="address")
    Position = relationship("Position", back_popilates="company")
    