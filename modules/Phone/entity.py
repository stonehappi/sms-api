from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship 
from core.database import Base
from core.entity import Entity


class Phone(Entity, Base):
    __tablename__ = "phone"
    number = Column(Integer)
    name = Column(String)
    
    contactId= Column(Integer, ForeignKey("Contact.id"))
    contact= relationship("Contact", back_populates="phones")