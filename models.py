from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from database import Base

# SQLAlchemy model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

# Pydantic models
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True  # <--- Correct way for SQLAlchemy compatibility
