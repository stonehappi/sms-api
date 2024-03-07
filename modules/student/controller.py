from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.student.entity import student
from modules.student.model import studentInsertRequest, studentUpdateRequest

router=APIRouter(prefix="/student",tags=["student"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(student).all();#    return"read all admin"

@router.post("/create")
def create(req: studentInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    Student = student(**req.dict())
    db.add(Student)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: studentUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(student).filter(student.id==item_id).first()
    if olderItem is None:
        return "student not found"
    else:
       
        olderItem.name=req.name
        olderItem.address=req.address
        olderItem.age=req.age
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    Student = db.query(student).filter(student.id == item_id).first()
    if Student is None:
        return "student not found"
    else:
        db.delete(Student)
        db.commit()
        return "delete successful"