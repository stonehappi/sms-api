from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base
from core.entity import Entity
from sqlalchemy.orm import relationship

class Contact(Entity, Base):
    __tablename__ = "contact"
    firstname = Column(String, index=True, name="Firstname")
    lastname = Column(String, name="Lastname")
    positionid = Column(Integer, ForeignKey("position.id"), name="PositionId")
    
    position = relationship("Position", back_populates="contacts")
    emails = relationship("Email", back_populates="contact")
    phones = relationship("Phone", back_populates="contact")
    
