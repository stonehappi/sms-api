from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.entity import Entity
from core.database import Base


class Phone(Entity, Base):
    __tablename__ = "Phone"
    #id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)
    name = Column(String, unique=True)

    Contact_id = Column(Integer, ForeignKey("Contact.id"))
    contact = relationship("Contact", back_populates= "phones")