from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from repositories.cliente_repository import ClienteRepository
from repositories.entrada_repository import EntradaRepository
from repositories.precio_sector_repository import PrecioSectorRepository
from repositories.venta_repository import VentaRepository
from services.pago_service import PagoService
from services.pasarela_pago import PasarelaSimulada
import schemas

router = APIRouter(tags=["Pagos"])


def get_pago_service(db: Session = Depends(get_db)) -> PagoService:
    """Arma el servicio inyectándole repositorios y pasarela."""
    return PagoService(
        EntradaRepository(db),
        PrecioSectorRepository(db),
        ClienteRepository(db),
        VentaRepository(db),
        PasarelaSimulada(),
    )


@router.post("/iniciar-pago", response_model=schemas.PagoResponse,
            status_code=201, summary="Pagar entradas y emitirlas")
def iniciar_pago(
    datos: schemas.IniciarPagoRequest,
    service: PagoService = Depends(get_pago_service),
):
    """Procesa el pago con la pasarela simulada. Si es aprobado crea la venta
    (Pagada) y emite las entradas. Errores: 402 (pago denegado), 409 (lugares
    ya no disponibles), 400 (cantidad inválida), 404 (cliente o sector inexistente).
    Tarjeta de prueba rechazada: número terminado en 0000."""
    return service.iniciar_pago(
        datos.cliente_id, datos.evento_id, datos.sector_id,
        datos.cantidad, datos.tarjeta,
    )


@router.post("/webhook-pagos")
def webhook_pagos():
    # TODO: la HU 2 se resuelve de forma síncrona en /iniciar-pago
    pass