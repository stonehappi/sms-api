from fastapi import APIRouter, Depends
from core.database import SessionLocal, get_db

from modules.position.entity import Position
from modules.position.model import positionInsertRequest, positionUpdateRequest

router=APIRouter(prefix="/position",tags=["position"])

@router.get("/read")
def read(db: SessionLocal = Depends(get_db)): # type: ignore
    return db.query(Position).all();#    return"read all admin"

@router.post("/create")
def create(req: positionInsertRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    position = Position(**req.dict())
    db.add(position)
    db.commit()
    return"your recording insert successfull"


@router.put("/update/{item_id}")
def update(item_id: int, req: positionUpdateRequest, db: SessionLocal = Depends(get_db)): # type: ignore
    olderItem = db.query(Position).filter(Position.id==item_id).first()
    if olderItem is None:
        return "position not found"
    else:
       
        olderItem.Name=req.Name
        olderItem.Companyid=req.Companyid
        db.commit()
        return "update successflly"


@router.delete("/delete/{item_id}")
def delete(item_id: int, db: SessionLocal = Depends(get_db)): # type: ignore
    position = db.query(position).filter(Position.id == item_id).first()
    if Position is None:
        return "Position not found"
    else:
        db.delete(Position)
        db.commit()
        return "delete successful"