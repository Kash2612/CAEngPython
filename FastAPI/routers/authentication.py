from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import Login, UserCreate  # Assuming schemas.py is in the routers folder
from database import get_db  # One level up to get the database modu
from . import models, JWTToken  # One level up to get models
from passlib.context import CryptContext




router = APIRouter(tags=['Authentication'])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

@router.post("/register")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is already registered")

    # Hash the password before saving it
    hashed_password = get_password_hash(user.password)

    # Create the new user
    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh to get the newly created ID

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
    }

@router.post('/login')
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()  # Fetch the first user

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid credentials")
    
    if not verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Incorrect Password")

    access_token = JWTToken.create_access_token(
        data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
