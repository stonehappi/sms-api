from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Contact.Entity import Contact
from modules.Contact.Model import ContactInsertRequest, ContactUpdateRequest


router = APIRouter(prefix="/Contact", tags=["Contact"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Contact).all()


@router.post("/create")
def creat(req: ContactInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Contact(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:ContactUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Contact).filter(Contact.id == item_id).first()
    if oldItem is None:
        return "Contact not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Contact).filter(Contact.id == item_id).first()
    if oldItem is None:
        return "Contact not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Contact has deleted"