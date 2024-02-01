from pydantic import BaseModel


class UserListResponse(BaseModel):
    id: int
    name: str


class UserInsertRequest(BaseModel):
    name: str


class UserUpdateRequest(BaseModel):
    name: str
