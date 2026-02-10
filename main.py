from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from models import User, UserCreate, UserResponse
from database import SessionLocal, engine, Base

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API with FastAPI & PostgreSQL")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------
# CREATE USER
# ------------------------
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ------------------------
# GET USERS (all or single)
# ------------------------
@app.get("/users", response_model=list[UserResponse])
def get_users(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    if user_id is not None:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return [user]  # wrap in list to match response_model
    return db.query(User).all()

# ------------------------
# UPDATE USER
# ------------------------
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password
    db.commit()
    db.refresh(user)
    return user

# ------------------------
# DELETE USER
# ------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# ------------------------
# Optional: Test DB Connection
# ------------------------
@app.on_event("startup")
def test_db_connection():
    try:
        conn = engine.connect()
        print("Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print("Error connecting to PostgreSQL:", e)
