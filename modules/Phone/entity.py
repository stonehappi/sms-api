
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from core.entity import Entity


class Phone(Entity, Base):
    __tablename__ = "phone"
    number = Column(String, index=True, name="Number")
    name = Column(String, name="Name")
    contactid = Column(Integer, ForeignKey("contact.id"), name="ContactId")
    phone1 = relationship("Contact", back_populates="phone_num")
    