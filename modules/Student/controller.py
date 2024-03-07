
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from modules.Student.entity import Student
from modules.Student.model import StudentInsertRequest, StudentUpdateResquest

router = APIRouter(prefix="/student", tags=["student"])

#
# Get Information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Student).all()

#
# Create/Insert New Student
#
@router.post("/create")
def create(req: StudentInsertRequest, db: Session = Depends(get_db)):
    new_Student = Student(**req.dict())
    db.add(new_Student)
    db.commit()
    return "New Student has been added!"

#
# Update/Change Student Information
#
@router.put("/update/{student_id}")
def update(student_id: int, req: StudentUpdateResquest, db: Session = Depends(get_db)):
    old_Student_info = db.query(Student).filter(Student.id == student_id).first()
    if old_Student_info is None:
        return "Student not found!"
    else:
        old_Student_info.name = req.name
        old_Student_info.address = req.address
        old_Student_info.age = req.age
        db.commit()
        db.refresh(old_Student_info)
        return "Student Info Has Been Updated!"

#
# Delete Student Record
#
@router.delete("/delete")
def delete(student_id: int, db: Session = Depends(get_db)):
    studentDel = db.query(Student).filter(Student.id == student_id).first()
    if studentDel:
        db.delete(studentDel)
        db.commit()
        return "Student Has Been Deleted!"
    return "Student Not Found!"