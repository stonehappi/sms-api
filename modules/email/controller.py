from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.email.entity import email
from modules.email.model import emailInsertRequest, emailUpdateRequest

router=APIRouter(prefix="/email",tags=["email"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(email).all();#    return"read all admin"

@router.post("/create")
def create(req: emailInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    email = email(**req.dict())
    db.add(email)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: emailUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(email).filter(email.id==item_id).first()
    if olderItem is None:
        return "email not found"
    else:
        olderItem.number=req.number
        olderItem.name=req.name
        olderItem.emailid=req.emailid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    email = db.query(email).filter(email.id == item_id).first()
    if email is None:
        return "email not found"
    else:
        db.delete(email)
        db.commit()
        return "delete successful"