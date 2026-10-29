from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.entrada_repository import EntradaRepository
from services.acceso_service import AccesoService
import schemas

router = APIRouter(prefix="/escanear-acceso", tags=["Control de Acceso"])


def get_acceso_service(db: Session = Depends(get_db)) -> AccesoService:
    """Arma el servicio inyectándole su repositorio."""
    return AccesoService(EntradaRepository(db))


@router.post("", response_model=schemas.AccesoResponse,
            summary="Escanear el QR de una entrada en la puerta")
def escanear_acceso(
    datos: schemas.EscaneoRequest,
    service: AccesoService = Depends(get_acceso_service),
):
    """Valida el QR. 200 'Acceso Permitido' si la entrada estaba Emitida (pasa a
    Utilizada y registra la hora). Errores: 409 (ya utilizada), 404 (QR inexistente),
    400 (ticket no emitido / falta de pago)."""
    return service.escanear(datos.codigo_qr)