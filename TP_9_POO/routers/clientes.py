from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Cliente
import schemas

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("", response_model=schemas.ClienteRead, status_code=201,
            summary="Crear un cliente")
def crear_cliente(datos: schemas.ClienteCreate, db: Session = Depends(get_db)):
    """Registra un nuevo Cliente (espectador que compra entradas)."""
    cliente = Cliente(nombre=datos.nombre, email=datos.email)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


@router.get("", response_model=List[schemas.ClienteRead],
            summary="Listar todos los clientes")
def listar_clientes(db: Session = Depends(get_db)):
    """Devuelve todos los Clientes registrados."""
    return db.query(Cliente).all()


@router.get("/{cliente_id}", response_model=schemas.ClienteRead,
            summary="Buscar un cliente por ID")
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    """Devuelve un Cliente por su ID, o 404 si no existe."""
    cliente = db.get(Cliente, cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente