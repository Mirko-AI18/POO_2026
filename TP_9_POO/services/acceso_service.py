from exceptions import TicketInvalido
from repositories.entrada_repository import EntradaRepository
import schemas


class AccesoService:
    """Caso de uso: validar un QR en la puerta. El repositorio se inyecta."""

    def __init__(self, entrada_repo: EntradaRepository):
        self.entrada_repo = entrada_repo

    def escanear(self, codigo_qr: str) -> schemas.AccesoResponse:
        entrada = self.entrada_repo.obtener_por_qr(codigo_qr)
        if entrada is None:
            raise TicketInvalido()

        # La entrada decide si puede usarse (y lanza el error que corresponda)
        entrada.marcar_utilizada()
        entrada = self.entrada_repo.guardar(entrada)

        return schemas.AccesoResponse(
            mensaje="Acceso Permitido",
            entrada_id=entrada.id,
            hora_ingreso=entrada.hora_ingreso,
        )