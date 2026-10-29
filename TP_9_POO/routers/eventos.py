from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Evento
from services.evento_service import EventoService
import schemas

router = APIRouter(prefix="/eventos", tags=["Eventos"])


@router.post("", response_model=schemas.EventoRead, status_code=201,
            summary="Crear un evento")
def crear_evento(datos: schemas.EventoCreate, db: Session = Depends(get_db)):
    """Crea un Evento en un Lugar, con el precio de cada sector.
    Genera automáticamente las Entradas (estado Disponible) según la
    capacidad de cada sector."""
    try:
        return EventoService(db).crear_evento(datos)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=List[schemas.EventoRead],
            summary="Listar todos los eventos")
def listar_eventos(db: Session = Depends(get_db)):
    """Devuelve todos los Eventos registrados."""
    return db.query(Evento).all()


@router.get("/{evento_id}", response_model=schemas.EventoRead,
            summary="Buscar un evento por ID")
def obtener_evento(evento_id: int, db: Session = Depends(get_db)):
    """Devuelve un Evento por su ID, o 404 si no existe."""
    evento = db.get(Evento, evento_id)
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento