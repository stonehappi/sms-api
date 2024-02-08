from pydantic import BaseModel


class UserListResponse(BaseModel):
    id: int
    username: str
    profile_photo: str
    password: str
    email: str
    age: int


class UserInsertRequest(BaseModel):
    username: str
    profile_photo: str
    password: str
    email: str
    age: int


class UserUpdateRequest(BaseModel):
    username: str
    profile_photo: str
    password: str
    email: str
    age: int
