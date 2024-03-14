
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Contact(Entity, Base):
    __tablename__ = "contact"
    firstname = Column(String, index=True, name="Firstname")
    lastname = Column(String, name="Lastname")
    positionid = Column(Integer, ForeignKey("position.id"), name="PositionId")
    
    position1 = relationship("Position", back_populates="contacts")
    
    emails = relationship("Email", back_populates="contact1")
    
    phone_num = relationship("Phone", back_populates="phone1")
    