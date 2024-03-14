from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.entity import Entity
from core.database import Base


class Email(Entity, Base):
    __tablename__ = "Email"
    #id = Column(Integer, primary_key=True)
    mail = Column(String, unique=True)
    name = Column(String, unique=True)

    Contact_id = Column(Integer, ForeignKey("Contact.id"))
    contact = relationship("Contact", back_populates= "emails")
    