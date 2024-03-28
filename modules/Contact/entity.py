from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base
from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "Contact"
    Firstname = Column(String)
    Lastname = Column(String)
    
    Positionid= Column(Integer, ForeignKey("position.id"))
    position= relationship("Position", back_populates="contacts")
    
    emails= relationship("Email", back_populates="contact")
    
    phones= relationship("Phone", back_populates="contact")
    
    