class DominioError(Exception):
    """Base de los errores de negocio. Cada uno sabe qué código HTTP le corresponde."""
    status_code = 400
    mensaje = "Error de negocio"

    def __init__(self, mensaje: str | None = None):
        if mensaje:
            self.mensaje = mensaje
        super().__init__(self.mensaje)


class CantidadInvalida(DominioError):
    status_code = 400
    mensaje = "La cantidad de entradas solicitadas debe ser mayor a cero"


class CapacidadInsuficiente(DominioError):
    status_code = 400
    mensaje = "Capacidad insuficiente o entradas no disponibles"


class SectorNoDisponibleEnEvento(DominioError):
    status_code = 404
    mensaje = "El evento no existe o no tiene ese sector"


class ClienteNoEncontrado(DominioError):
    status_code = 404
    mensaje = "Cliente no encontrado"


class EntradasNoDisponibles(DominioError):
    status_code = 409
    mensaje = "Los lugares seleccionados ya no se encuentran disponibles"


class PagoDenegado(DominioError):
    status_code = 402
    mensaje = "Pago denegado"


class TicketInvalido(DominioError):
    status_code = 404
    mensaje = "Ticket Inválido o Inexistente"


class EntradaYaUtilizada(DominioError):
    status_code = 409
    mensaje = "Entrada ya utilizada"


class TicketNoEmitido(DominioError):
    status_code = 400
    mensaje = "Ticket no emitido / Falta de pago"