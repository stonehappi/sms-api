from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db, SessionLocal
from modules. Student.model import StudentUpdateRequest, StudentInsertRequest, StundentListRespone
from modules.Student.entity import Student 

router = APIRouter(prefix="/Student", tags=["Stduent"])


@router.post("/create/")
def create(request: StudentInsertRequest, db: Session = Depends(get_db)):
    item = Student(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return "Created!!"

@router.get("/read/")
def get(db: Session = Depends(get_db)):
    Students = db.query(Student).all()
    return Students

@router.get("/update/{item.id}")
def update(item_id: int, request:StudentUpdateRequest, db: Session = Depends(get_db)):
    old_item= db.query(Student).filter(Student.id == item_id).first()
    if old_item:
        old_item.name = request.name
        old_item.address = request.address
        old_item.age = request.age
        db.commit()
        db.refresh(old_item)
        return old_item
    return {"message": "yoooo your item not found dude"}

@router. delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Student).filter(Student.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "item already deleted in your Data"}
    return {"message": "item cannot found ma boy"}
