from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class LugarCreate(BaseModel):
    """Datos que envía el cliente para crear un Lugar."""
    nombre: str
    direccion: str


class LugarRead(BaseModel):
    """Datos que devuelve la API al leer un Lugar."""
    id: int
    nombre: str
    direccion: str | None = None

    model_config = ConfigDict(from_attributes=True)


class SectorCreate(BaseModel):
    """Datos que envía el cliente para crear un Sector."""
    nombre: str
    capacidad_maxima: int = Field(gt=0)
    lugar_id: int


class SectorRead(BaseModel):
    """Datos que devuelve la API al leer un Sector."""
    id: int
    nombre: str
    capacidad_maxima: int
    lugar_id: int

    model_config = ConfigDict(from_attributes=True)


class ClienteCreate(BaseModel):
    """Datos que envía el cliente para registrarse."""
    nombre: str
    email: str


class ClienteRead(BaseModel):
    """Datos que devuelve la API al leer un Cliente."""
    id: int
    nombre: str
    email: str | None = None

    model_config = ConfigDict(from_attributes=True)


class PrecioSectorCreate(BaseModel):
    """Precio que la productora fija para un sector en este evento."""
    sector_id: int
    precio: float = Field(gt=0)


class PrecioSectorRead(BaseModel):
    sector_id: int
    precio: float

    model_config = ConfigDict(from_attributes=True)


class EventoCreate(BaseModel):
    """Datos para crear un Evento, con el precio de cada sector del lugar."""
    nombre: str
    fecha: datetime | None = None
    lugar_id: int
    precios: List[PrecioSectorCreate]


class EventoRead(BaseModel):
    """Datos que devuelve la API al leer un Evento."""
    id: int
    nombre: str
    fecha: datetime | None = None
    lugar_id: int
    precios: List[PrecioSectorRead] = []

    model_config = ConfigDict(from_attributes=True)


class CotizacionRequest(BaseModel):
    """Lo que elige el espectador: evento, sector y cantidad."""
    evento_id: int
    sector_id: int
    cantidad: int


class CotizacionResponse(BaseModel):
    """Resultado de la cotización."""
    evento_id: int
    sector_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float
    total: float


class DatosTarjeta(BaseModel):
    """Datos de la tarjeta que se envían a la pasarela."""
    numero: str
    titular: str
    vencimiento: str
    cvv: str


class IniciarPagoRequest(BaseModel):
    """Lo que envía el cliente para pagar."""
    cliente_id: int
    evento_id: int
    sector_id: int
    cantidad: int
    tarjeta: DatosTarjeta


class EntradaRead(BaseModel):
    """Entrada emitida, con su código QR."""
    id: int
    sector_id: int
    estado: str
    codigo_qr: str

    model_config = ConfigDict(from_attributes=True)


class PagoResponse(BaseModel):
    """Resultado de un pago exitoso."""
    venta_id: int
    estado: str
    total: float
    entradas: List[EntradaRead]


class EscaneoRequest(BaseModel):
    """Código QR que lee el acomodador."""
    codigo_qr: str


class AccesoResponse(BaseModel):
    """Resultado de un acceso permitido."""
    mensaje: str
    entrada_id: int
    hora_ingreso: datetime