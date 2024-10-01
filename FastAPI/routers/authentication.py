from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import Login  # Assuming schemas.py is in the routers folder
from database import get_db  # One level up to get the database modu
from . import models  # One level up to get models



router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()  # Fetch the first user

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")

    return user
