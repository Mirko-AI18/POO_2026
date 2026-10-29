from exceptions import (
    CantidadInvalida,
    ClienteNoEncontrado,
    EntradasNoDisponibles,
    PagoDenegado,
    SectorNoDisponibleEnEvento,
)
from models import Venta
from repositories.cliente_repository import ClienteRepository
from repositories.entrada_repository import EntradaRepository
from repositories.precio_sector_repository import PrecioSectorRepository
from repositories.venta_repository import VentaRepository
from services.pasarela_pago import PasarelaPago, ResultadoPago
import schemas


class PagoService:
    """Caso de uso: pagar entradas y emitirlas. Todas las dependencias se inyectan."""

    def __init__(
        self,
        entrada_repo: EntradaRepository,
        precio_repo: PrecioSectorRepository,
        cliente_repo: ClienteRepository,
        venta_repo: VentaRepository,
        pasarela: PasarelaPago,
    ):
        self.entrada_repo = entrada_repo
        self.precio_repo = precio_repo
        self.cliente_repo = cliente_repo
        self.venta_repo = venta_repo
        self.pasarela = pasarela

    def iniciar_pago(
        self,
        cliente_id: int,
        evento_id: int,
        sector_id: int,
        cantidad: int,
        tarjeta: schemas.DatosTarjeta,
    ) -> schemas.PagoResponse:
        if cantidad <= 0:
            raise CantidadInvalida()

        cliente = self.cliente_repo.obtener(cliente_id)
        if cliente is None:
            raise ClienteNoEncontrado()

        precio_sector = self.precio_repo.obtener(evento_id, sector_id)
        if precio_sector is None:
            raise SectorNoDisponibleEnEvento()

        # 1. Se re-verifica la disponibilidad ANTES de consultar a la pasarela
        entradas = self.entrada_repo.obtener_disponibles(
            evento_id, sector_id, cantidad
        )
        if len(entradas) < cantidad:
            raise EntradasNoDisponibles()

        # 2. Se consulta a la pasarela (abstracción inyectada)
        total = precio_sector.calcular_subtotal(cantidad)
        resultado = self.pasarela.procesar(tarjeta.numero, total)
        if resultado != ResultadoPago.APROBADO:
            raise PagoDenegado()  # no se modificó nada: las entradas siguen Disponibles

        # 3. Pago aprobado: se crea la venta y cada entrada se emite sola
        venta = Venta(cliente_id=cliente.id, estado="Pagada", total=total)
        for entrada in entradas:
            entrada.emitir(venta)
        venta = self.venta_repo.guardar(venta)

        return schemas.PagoResponse(
            venta_id=venta.id,
            estado=venta.estado,
            total=venta.total,
            entradas=venta.entradas,
        )