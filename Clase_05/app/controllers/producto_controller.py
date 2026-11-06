from fastapi import APIRouter, HTTPException, Query, status

from app.db.database import SessionDep
from app.dependencies.auth import CurrentUser
from app.schemas.producto import ProductoCreate, ProductoUpdate
from app.services import producto_service


router = APIRouter(tags=["Productos"])

@router.get("/productos")
def obtener_productos(
    current_user: CurrentUser,
    session: SessionDep
):
    return producto_service.obtener_productos(
        current_user.id,
        session
    )


@router.post(
    "/productos",
    status_code=status.HTTP_201_CREATED
)
def crear_producto(
    data: ProductoCreate,
    current_user: CurrentUser,
    session: SessionDep
):
    return producto_service.crear_producto(
        data,
        current_user.id,
        session
    )


@router.get("/productos/{id_producto}")
def obtener_producto(
    id_producto: int,
    current_user: CurrentUser,
    session: SessionDep
):
    producto = producto_service.obtener_producto(
        id_producto,
        current_user.id,
        session
    )

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto

@router.put("/productos/{id_producto}")
def actualizar_producto(
    id_producto: int,
    data: ProductoUpdate,
    current_user: CurrentUser,
    session: SessionDep
):
    producto = producto_service.actualizar_producto(
        id_producto,
        data,
        current_user.id,
        session
    )

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return producto


@router.delete("/productos/{id_producto}")
def eliminar_producto(
    id_producto: int,
    current_user: CurrentUser,
    session: SessionDep
):
    producto = producto_service.eliminar_producto(
        id_producto,
        current_user.id,
        session
    )

    if producto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return {"mensaje": f"Producto {id_producto} eliminado correctamente"}