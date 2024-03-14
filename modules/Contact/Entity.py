from sqlalchemy import Column, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship
from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "Contact"
    FirstName = Column(String)
    LastName = Column(String)
    PositionId = Column(Integer, ForeignKey("Position.id"))
    position = relationship("Position", back_populates="contacts")
    emails = relationship("Email", back_populates="contact")
    phones = relationship("Phone", back_populates="contact")
    
    