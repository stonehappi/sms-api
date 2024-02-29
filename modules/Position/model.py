

from pydantic import BaseModel


class InsertNewPosition(BaseModel):
    name: str
    companyid: int

class UpdatePosition(BaseModel):
    name: str
    companyid: int
