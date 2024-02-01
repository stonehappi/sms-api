from sqlalchemy import Column, Integer, DateTime,Enum
from core.status import EStatus


class Entity:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    status = Column(Enum(EStatus), default=1)
