from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.models.user import User
from app.schemas.user import UserResponse


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return users