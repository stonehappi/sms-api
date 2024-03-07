from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.entity import Entity
from core.database import Base


class Position(Entity, Base):
    __tablename__ = "Position"
    #id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
 
    Company_id = Column(Integer, ForeignKey("Company.id"))
    company = relationship("Company", back_populates="positions")

    Contact = relationship("Contact", back_populates= "position")