from fastapi import APIRouter, Depends

from core.database import SessionLocal, get_db
from modules.admin.entity import Admin
router=APIRouter(prefix="/admin",tags=["admin"])
@router.get("")
def get(db: SessionLocal = Depends(get_db)):
    return db.query(Admin).all();#    return"read all admin"
def create():
    return"create all admin"
def update():
    return"update all admin"
def delete():
    return"delete all admin"
