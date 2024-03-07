
from pydantic import BaseModel

class StundentListRespone(BaseModel): # type: ignore
    name: str
    address: str
    age: int
class StudentInsertRequest(BaseModel): # type: ignore
    name: str
    address: str
    age: int
class StudentUpdateRequest(BaseModel): # type: ignore
    name: str
    address: str
    age: int