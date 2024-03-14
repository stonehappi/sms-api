
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Email(Entity, Base):
    __tablename__ = "email"
    mail = Column(String, index=True, name="Mail")
    name = Column(String, name="Name")
    
    contactid = Column(Integer, ForeignKey("contact.id"), name="ContactId")
    contact1 = relationship("Contact", back_populates="emails")
    