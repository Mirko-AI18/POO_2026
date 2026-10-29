from exceptions import (
    CantidadInvalida,
    CapacidadInsuficiente,
    SectorNoDisponibleEnEvento,
)
from repositories.entrada_repository import EntradaRepository
from repositories.precio_sector_repository import PrecioSectorRepository
import schemas


class CotizacionService:
    """Caso de uso: cotizar entradas. Los repositorios se inyectan por constructor."""

    def __init__(
        self,
        entrada_repo: EntradaRepository,
        precio_repo: PrecioSectorRepository,
    ):
        self.entrada_repo = entrada_repo
        self.precio_repo = precio_repo

    def cotizar(
        self, evento_id: int, sector_id: int, cantidad: int
    ) -> schemas.CotizacionResponse:
        # 1. Validación de datos (se rechaza de inmediato)
        if cantidad <= 0:
            raise CantidadInvalida()

        # 2. ¿Existe ese sector para ese evento? (y su precio)
        precio_sector = self.precio_repo.obtener(evento_id, sector_id)
        if precio_sector is None:
            raise SectorNoDisponibleEnEvento()

        # 3. Validación de stock
        disponibles = self.entrada_repo.contar_disponibles(evento_id, sector_id)
        if disponibles < cantidad:
            raise CapacidadInsuficiente()

        # 4. El cálculo lo hace el experto: el PrecioSector
        subtotal = precio_sector.calcular_subtotal(cantidad)

        return schemas.CotizacionResponse(
            evento_id=evento_id,
            sector_id=sector_id,
            cantidad=cantidad,
            precio_unitario=precio_sector.precio,
            subtotal=subtotal,
            total=subtotal,
        )