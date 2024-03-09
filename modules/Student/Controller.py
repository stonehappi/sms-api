from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Student.Entity import Student
from modules.Student.Model import StudentInsertRequest, StudentUpdateRequest


router = APIRouter(prefix="/Student", tags=["Student"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Student).all()


@router.post("/create")
def creat(req: StudentInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Student(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:StudentUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Student).filter(Student.id == item_id).first()
    if oldItem is None:
        return "Student not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        oldItem.age = req.age
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Student).filter(Student.id == item_id).first()
    if oldItem is None:
        return "Student not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Student has deleted"