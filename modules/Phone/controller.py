from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.Phone.entity import Phone
from modules.Phone.model import phoneInsertRequest, phoneUpdateRequest

router=APIRouter(prefix="/phone",tags=["phone"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Phone).all();#    return"read all admin"

@router.post("/create")
def create(req: phoneInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    phone = Phone(**req.dict())
    db.add(phone)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: phoneUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(Phone).filter(Phone.id==item_id).first()
    if olderItem is None:
        return "phone not found"
    else:
        olderItem.number=req.number
        olderItem.name=req.name
        olderItem.contactid=req.contactid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    phone = db.query(Phone).filter(Phone.id == item_id).first()
    if phone is None:
        return "phone not found"
    else:
        db.delete(phone)
        db.commit()
        return "delete successful"