
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.staff.entity import Staff
from modules.staff.model import NewStaff_InsertionRequest, Staff_DeleteRequest, Staff_UpdateRequest


router = APIRouter(prefix="/staff", tags=["staff"])

@router.get("/read")
def gets(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Staff).all()

#@router.get("/get-salary_{fullname}")
#def gets(get_salary: ):
    #return get_salary

@router.post("/create")
def create(req: NewStaff_InsertionRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    new_staff = Staff(**req.dict())
    db.add(new_staff)
    db.commit()
    return "New Staff has been added!"

@router.get("/update")
def update(req: Staff_UpdateRequest):
    return req

@router.get("/delete")
def delete(req: Staff_DeleteRequest):
    return req
