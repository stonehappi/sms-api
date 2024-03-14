from pydantic import BaseModel


class PhoneListResponse(BaseModel):
    id: int
    number: str
    name: str
    contact_id: int


class PhoneInsertRequest(BaseModel):
    number: str
    name: str
    contact_id: int


class PhoneUpdateRequest(BaseModel):
    number: str
    name: str
    contact_id: int
