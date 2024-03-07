from pickle import NONE
from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.Email.Entity import Email
from modules.Email.Model import EmailInsertRequest, EmailUpdateRequest


router = APIRouter(prefix="/Email", tags=["Email"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Email).all()


@router.post("/create")
def creat(req: EmailInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    item = Email(**req.dict())
    db.add(item)
    db.commit()
    return "inserted"

@router.put("/update/{item_id}")
def update(
    item_id: int,req:EmailUpdateRequest, db:SessionLocal = Depends(get_db) # type: ignore
):
    oldItem = db.query(Email).filter(Email.id == item_id).first()
    if oldItem is None:
        return "Email not Found"
    else:
        oldItem.name= req.name
        oldItem.address = req.address
        db.commit()
        return "Update Successfull"
    
@router.delete("/dlete/{item_id}")
def delete(
    item_id: int, db:SessionLocal = Depends(get_db) # type: ignore
):      
    oldItem = db.query(Email).filter(Email.id == item_id).first()
    if oldItem is None:
        return "Email not found"
    else : 
        db.delete(oldItem)
        db.commit()
        return "Email has deleted"