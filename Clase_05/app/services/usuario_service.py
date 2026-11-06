from sqlmodel import select

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.core.security import hash_password, verify_password
from sqlmodel import select, or_

def registrar_usuario(data: UsuarioCreate, session):
    usuario_existente = session.exec(
        select(Usuario).where(
            or_(
                Usuario.username == data.username,
                Usuario.email == data.email
            )
        )
    ).first()

    if usuario_existente:
        return None

    usuario = Usuario(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario


def autenticar_usuario(username: str, password: str, session):
    usuario = session.exec(
        select(Usuario).where(
            Usuario.username == username
        )
    ).first()

    print("👉 Usuario recibido:", repr(username))
    print("👉 Usuario encontrado en BD:", usuario)

    if usuario is None:
        return None

    print("👉 ¿Contraseña correcta?:", verify_password(password, usuario.hashed_password))

    if not verify_password(password, usuario.hashed_password):
        return None

    return usuario