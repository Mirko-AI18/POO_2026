from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Lugar
import schemas

router = APIRouter(prefix="/lugares", tags=["Lugares"])


@router.post("", response_model=schemas.LugarRead, status_code=201,
            summary="Crear un lugar")
def crear_lugar(datos: schemas.LugarCreate, db: Session = Depends(get_db)):
    """Registra un nuevo Lugar (estadio, teatro, etc.)."""
    lugar = Lugar(nombre=datos.nombre, direccion=datos.direccion)
    db.add(lugar)
    db.commit()
    db.refresh(lugar)
    return lugar


@router.get("", response_model=List[schemas.LugarRead],
            summary="Listar todos los lugares")
def listar_lugares(db: Session = Depends(get_db)):
    """Devuelve todos los Lugares registrados."""
    return db.query(Lugar).all()


@router.get("/{lugar_id}", response_model=schemas.LugarRead,
            summary="Buscar un lugar por ID")
def obtener_lugar(lugar_id: int, db: Session = Depends(get_db)):
    """Devuelve un Lugar por su ID, o 404 si no existe."""
    lugar = db.get(Lugar, lugar_id)
    if lugar is None:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return lugar