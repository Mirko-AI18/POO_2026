from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Lugar, Sector
import schemas

router = APIRouter(prefix="/sectores", tags=["Sectores"])


@router.post("", response_model=schemas.SectorRead, status_code=201,
            summary="Crear un sector")
def crear_sector(datos: schemas.SectorCreate, db: Session = Depends(get_db)):
    """Registra un Sector dentro de un Lugar. La capacidad máxima la define el sector."""
    if db.get(Lugar, datos.lugar_id) is None:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    sector = Sector(
        nombre=datos.nombre,
        capacidad_maxima=datos.capacidad_maxima,
        lugar_id=datos.lugar_id,
    )
    db.add(sector)
    db.commit()
    db.refresh(sector)
    return sector


@router.get("", response_model=List[schemas.SectorRead],
            summary="Listar todos los sectores")
def listar_sectores(db: Session = Depends(get_db)):
    """Devuelve todos los Sectores registrados."""
    return db.query(Sector).all()


@router.get("/{sector_id}", response_model=schemas.SectorRead,
            summary="Buscar un sector por ID")
def obtener_sector(sector_id: int, db: Session = Depends(get_db)):
    """Devuelve un Sector por su ID, o 404 si no existe."""
    sector = db.get(Sector, sector_id)
    if sector is None:
        raise HTTPException(status_code=404, detail="Sector no encontrado")
    return sector