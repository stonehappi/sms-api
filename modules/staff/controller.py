
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from core.database import get_db
from modules.staff.entity import Staff
from modules.staff.model import NewStaff_InsertionRequest, Staff_UpdateRequest

router = APIRouter(prefix="/staff", tags=["staff"])

#
# Get all staff information
#
@router.get("/read")
def gets(db: Session = Depends(get_db)):
    return db.query(Staff).all()

# 
# Get only one staff information
#
@router.get("/read/{item_id}")
def get(item_id: int, db: Session = Depends(get_db)):
    oldItem = db.query(Staff).filter(Staff.id == item_id).first()
    if oldItem is None:
        return "Staff no found!"
    else:
        return oldItem 

#
# Get staff salary information
#
@router.get("/get-salary_{Item_id}")
def gets(item_id: int, db: Session = Depends(get_db)):
    staff = db.query(Staff).filter(Staff.id == item_id).first()
    if staff is None:
        return "Staff no found!"
    else:
        return {
            "Fullname": staff.fullname,
            "Salary": staff.salary
        }

#
# Create/Insert new staff or add new staff
#
@router.post("/create")
def create(req: NewStaff_InsertionRequest, db: Session = Depends(get_db)):
    new_staff = Staff(**req.dict())
    db.add(new_staff)
    db.commit()
    return "New Staff has been added!"

#
# Update/Change information of staff in the database
#
@router.put("/update/{item_id}")
def update(item_id: int, req: Staff_UpdateRequest, db: Session = Depends(get_db)):
    oldItem = db.query(Staff).filter(Staff.id == item_id).first()
    if oldItem is None:
        return "Staff no found!!"
    else: 
        oldItem.salary = req.salary
        oldItem.position = req.position
        oldItem.department = req.department
        oldItem.location = req.location
        oldItem.email = req.email
        db.commit()
        db.refresh(oldItem)
        # oldItem = Staff(**req.dict())
        # db.add(oldItem)
        # db.commit()
        return "Staff Info Has Been Updated!!"

#
# Delete the information of the Staff
#
@router.delete("/delete")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Staff).filter(Staff.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return "Staff Has Been Deleted!!"
    return "Staff no found!!"
