from sqlmodel import SQLModel, Field
#from pydantic import BaseModel, EmailStr, Field


class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(
        min_length=3,
        max_length=50,
        unique=True,
        index=True
    )
    email: str = Field(unique=True, index=True)
    hashed_password:str