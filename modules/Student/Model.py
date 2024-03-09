from pydantic import BaseModel


class StudentInsertRequest(BaseModel):
    name: str
    address : str
    age : int
class StudentUpdateRequest(BaseModel):
    name : str
    address : str
    age : int
class StudentRespon(BaseModel):
    name : str
    address : str
    age : int