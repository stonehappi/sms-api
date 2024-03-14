from pydantic import BaseModel


class ContactListResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    position_id: int


class ContactInsertRequest(BaseModel):
    firstname: str
    lastname: str
    position_id: int


class ContactUpdateRequest(BaseModel):
    firstname: str
    lastname: str
    position_id: int
