from uuid import UUID

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.teacher.entity import Teacher
from modules.teacher.model import TeacherInsertRequest, TeacherUpdateRequest

router = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get("")
def gets(db: Session = Depends(get_db)):
    return db.query(Teacher).all()


@router.get("/{item_id}")
def get(item_id: UUID):
    return f"get by id = {item_id}"


@router.post("")
def create(item: TeacherInsertRequest):
    return f"create new user {item}"


@router.put("/{item_id}")
def update(item_id: UUID, item: TeacherUpdateRequest):
    return f"update user id = {item_id} and value = {item}"


@router.delete("/{item_id}")
def delete(item_id: int):
    return f"delete user id = {item_id}"
