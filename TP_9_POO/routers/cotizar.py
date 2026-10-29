from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.entrada_repository import EntradaRepository
from repositories.precio_sector_repository import PrecioSectorRepository
from services.cotizacion_service import CotizacionService
import schemas

router = APIRouter(prefix="/cotizar", tags=["Cotización"])


def get_cotizacion_service(db: Session = Depends(get_db)) -> CotizacionService:
    """Arma el servicio inyectándole sus repositorios."""
    return CotizacionService(EntradaRepository(db), PrecioSectorRepository(db))


@router.post("", response_model=schemas.CotizacionResponse,
            summary="Cotizar entradas")
def cotizar(
    datos: schemas.CotizacionRequest,
    service: CotizacionService = Depends(get_cotizacion_service),
):
    """Calcula el costo total de comprar `cantidad` entradas de un sector
    para un evento. Errores: 400 (cantidad inválida o capacidad insuficiente),
    404 (el evento no tiene ese sector)."""
    return service.cotizar(datos.evento_id, datos.sector_id, datos.cantidad)