from abc import ABC, abstractmethod
from enum import Enum


class ResultadoPago(str, Enum):
    APROBADO = "Aprobado"
    RECHAZADO = "Rechazado"


class PasarelaPago(ABC):
    """Abstracción de la pasarela. El servicio depende de esto, no de una pasarela concreta."""

    @abstractmethod
    def procesar(self, numero_tarjeta: str, monto: float) -> ResultadoPago:
        ...


class PasarelaSimulada(PasarelaPago):
    """Pasarela de pruebas: rechaza las tarjetas que terminan en 0000
    (simula fondos insuficientes) y aprueba el resto."""

    def procesar(self, numero_tarjeta: str, monto: float) -> ResultadoPago:
        if numero_tarjeta.endswith("0000"):
            return ResultadoPago.RECHAZADO
        return ResultadoPago.APROBADO