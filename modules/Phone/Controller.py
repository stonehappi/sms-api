from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Phone.Entity import Phone
from modules.Phone.Model import PhoneInsertRequest, PhoneUpdateRequest


router = APIRouter(prefix="/Phone", tags=["Phone"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Phone).all()


@router.post("/create")
def creat(req: PhoneInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Phone(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:PhoneUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Phone).filter(Phone.id == item_id).first()
    if oldItem is None:
        return "Phone not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Phone).filter(Phone.id == item_id).first()
    if oldItem is None:
        return "Phone not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Phone has deleted"