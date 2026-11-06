from sqlmodel import SQLModel, Field
from pydantic import BaseModel, EmailStr, Field


class UsuarioCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr = Field(unique=True)
    password: str = Field(min_length=8)


class Token(SQLModel):
    access_token: str
    token_type: str