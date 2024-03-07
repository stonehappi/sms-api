
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from core.database import get_db
from modules.student.entity import Student
from modules.student.model import StudentInsertRequest, StudentListResponse, StudentUpdateRequest

router = APIRouter(prefix="/Student", tags=["Student"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    positions = db.query(Student).all()
    return positions


@router.post("/create")
def create(request: StudentInsertRequest, db: Session = Depends(get_db)):
    item = Student(**request.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return StudentInsertRequest(**item.__dict__)

@router.put("/update/{item_id}")
def update(item_id: int, request: StudentUpdateRequest, db: Session = Depends(get_db)):
    old_item = db.query(Student).filter(Student.id == item_id).first()
    if old_item is None:
        # old_item.update(request.dict())
        return {"message": "Item not found"}
    else:
        old_item.name = request.name
        old_item.address = request.address
        old_item.age = request.age
        db.commit()
        db.refresh(old_item)
        return "Updated"
    

@router.delete("/delete/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Student).filter(Student.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}