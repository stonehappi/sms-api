from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship 

from core.database import Base
from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "Email"
    mails = Column(String)
    namelocation = Column(String)
    status = Column(String)
    
    contactId= Column(Integer, ForeignKey("Contact.id"))
    contact= relationship("Contact", back_populates="emails")
    