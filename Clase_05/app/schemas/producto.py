from sqlmodel import SQLModel, Field

class ProductoCreate(SQLModel):
    name: str
    description: str
    price: float
    stock:int

class ProductoUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=300)
    price: float | None = Field(default=None, gt=0)
    stock: int | None = Field(default=None, ge=0)