import dbm
from shelve import DbfilenameShelf
from fastapi import APIRouter, Depends, HTTPException

from core.database import SessionLocal, get_db
from modules.admin.entity import Admin
from modules.admin.model import AdminInsertRequest, AdminUpdateRequest
router=APIRouter(prefix="/admin",tags=["admin"])


@router.get("/read")
def read(db: SessionLocal = Depends(get_db)):
    return db.query(Admin).all();#    return"read all admin"

@router.post("create/{item_id}")
def create(req: AdminInsertRequest):
    return req


    admin = Admin(**req.dict())
    db.add(admin)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: AdminUpdateRequest, db: SessionLocal = Depends(get_db)):
    olderItem = db.query(Admin).filter(Admin.id==item_id).first()
    if olderItem is None:
        return "admin not found"
    else:
        olderItem.fullname=req.fullname
        olderItem.password=req.password
        olderItem.devise=req.devise
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.id == item_id).first()
    if admin is None:
        return "admin not found"
    else:
        db.delete(admin)
        db.commit()
        return "delete successful"