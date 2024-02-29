from uuid import UUID

from fastapi import Depends, APIRouter
from modules.Department.entity import Department
from sqlalchemy.orm import Session
from core.database import SessionLocal, get_db
from modules.Department.model import DepartmentInsertRequest, DepartmentUpdateRequest

router = APIRouter(prefix="/Department", tags=["Department"])


@router.get("/read")
def read(db: Session = Depends(get_db)):
    return db.query(Department).all()


@router.post("/create")
def creat(req: DepartmentInsertRequest):
    return req


@router.put("/update/{item_id}")
def update(
    item_id: int,req:DepartmentUpdateRequest, db:SessionLocal = Depends(get_db)
):
    oldItem = db.query(Department).filter(Department.id == item_id).first()
    if oldItem is None:
        return "Department not Found"
    else:
        oldItem.floor= req.floor
        oldItem.room = req.room
        oldItem.short_name = req.short_name
        db.commit()
        return "Update Successfull"
@router.get("/dlete/{item_id}")
def delete(
    item_id: int,req:DepartmentUpdateRequest, db:SessionLocal = Depends(get_db)
):      
    oldItem = db.query(Department).filter(Department.id == item_id).first()
    if oldItem is none:
        return "Department not found"
    else : 
        bd.delete(oldItem)
        bd.comit()
        return "Department has deleted"




















