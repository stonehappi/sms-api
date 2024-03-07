

from pydantic import BaseModel


class InsertNewPhone(BaseModel):
    number: str
    name: str
    contactid: int

class UpdatePhone(BaseModel):
    number: str
    name: str
    contactid: int
