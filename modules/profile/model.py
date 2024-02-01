from pydantic import BaseModel


class ProfileListResponse(BaseModel):
    id: int
    name: str


class ProfileInsertRequest(BaseModel):
    name: str


class ProfileUpdateRequest(BaseModel):
    name: str
