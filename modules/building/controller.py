from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.building.entity import Building
from modules.building.model import BuildingInsertRequest, BuildingUpdateRequest


router = APIRouter(prefix="/building", tags=["building"])


@router.get("/read")
def read(db: SessionLocal = Depends(get_db)):
    return db.query(Building).all()


@router.post("/create")
def create(req: BuildingInsertRequest, db: SessionLocal = Depends(get_db)):
    building = Building(**req.dict())
    db.add(building)
    db.commit()
    return "Your record insert successfully"


@router.put("/update/{item_id}")
def update(
    item_id: int, req: BuildingUpdateRequest, db: SessionLocal = Depends(get_db)
):
    # get the existed building from database by id
    oldItem = db.query(Building).filter(Building.id == item_id).first()
    if oldItem is None:
        return "Building not Found!"
    else:
        oldItem.floor = req.floor
        oldItem.roos = req.roos
        oldItem.date = req.date
        oldItem.draft = req.draft
        db.commit()
        db.refresh(oldItem)
        return "Update Successful"


@router.get("/delete")
def delete():
    return "delete teacher"


@router.get("/sr")
def sr():
    return "go to SR"


# from uuid import UUID

# from fastapi import Depends, APIRouter
# from sqlalchemy.orm import Session
# from core.database import get_db
# from modules.teacher.entity import Teacher
# from modules.teacher.model import TeacherInsertRequest, TeacherUpdateRequest

# router = APIRouter(prefix="/teacher", tags=["teacher"])


# @router.get("")
# def gets(db: Session = Depends(get_db)):
#     return db.query(Teacher).all()


# @router.get("/{item_id}")
# def get(item_id: UUID):
#     return f"get by id = {item_id}"


# @router.post("")
# def create(item: TeacherInsertRequest):
#     return f"create new user {item}"


# @router.put("/{item_id}")
# def update(item_id: UUID, item: TeacherUpdateRequest):
#     return f"update user id = {item_id} and value = {item}"


# @router.delete("/{item_id}")
# def delete(item_id: int):
#     return f"delete user id = {item_id}"
