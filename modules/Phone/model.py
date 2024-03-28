from pydantic import BaseModel 

class PhoneListResponse(BaseModel):
    id: int
    number: int
    name: str
    contactId: int
class PhoneInsertRequest(BaseModel):  # type: ignore
    id: int
    number: int
    name: str
    contactId: int
class PhoneUpdateRequest(BaseModel):  # type: ignore
    id: int
    number: int
    name: str
    contactId: int