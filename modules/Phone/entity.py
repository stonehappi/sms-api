from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base
from core.entity import Entity
from sqlalchemy.orm import relationship

class Phone(Entity, Base):
    __tablename__="phone"
    number = Column(String)
    name  = Column(String, name="Name", index=True, unique=True, nullable=False)
    Contactid = Column(Integer, ForeignKey("contact.id"), name="contactid")
    contact = relationship("Contact", back_populates="phones")