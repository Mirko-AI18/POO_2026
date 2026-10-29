from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from exceptions import (
    EntradasNoDisponibles,
    EntradaYaUtilizada,
    TicketNoEmitido,
)


class Lugar(Base):
    __tablename__ = "lugares"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String)

    sectores = relationship("Sector", back_populates="lugar")


class Sector(Base):
    __tablename__ = "sectores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    lugar_id = Column(Integer, ForeignKey("lugares.id"))

    lugar = relationship("Lugar", back_populates="sectores")


class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha = Column(DateTime)
    lugar_id = Column(Integer, ForeignKey("lugares.id"))

    lugar = relationship("Lugar")
    precios = relationship("PrecioSector", back_populates="evento")


class PrecioSector(Base):
    """Precio de un Sector para un Evento en particular."""
    __tablename__ = "precios_sector"
    id = Column(Integer, primary_key=True, index=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    sector_id = Column(Integer, ForeignKey("sectores.id"), nullable=False)
    precio = Column(Float, nullable=False)

    evento = relationship("Evento", back_populates="precios")
    sector = relationship("Sector")

    def calcular_subtotal(self, cantidad: int) -> float:
        """El precio es quien sabe cuánto cuestan N entradas (Experto)."""
        return self.precio * cantidad


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String)


class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String)  # Pendiente, Pagada, Cancelada
    total = Column(Float)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente")
    entradas = relationship("Entrada", back_populates="venta")


class Entrada(Base):
    __tablename__ = "entradas"
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(String)  # Disponible, Reservada, Emitida, Utilizada
    codigo_qr = Column(String, unique=True, index=True)
    hora_ingreso = Column(DateTime, nullable=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    sector_id = Column(Integer, ForeignKey("sectores.id"))
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=True)

    evento = relationship("Evento")
    sector = relationship("Sector")
    venta = relationship("Venta", back_populates="entradas")

    def emitir(self, venta: "Venta") -> None:
        """La entrada sabe cuándo puede emitirse: solo si está Disponible (Experto)."""
        if self.estado != "Disponible":
            raise EntradasNoDisponibles()
        self.estado = "Emitida"
        self.venta = venta

    def marcar_utilizada(self) -> None:
        """La entrada sabe cuándo se puede usar: solo si está Emitida (Experto)."""
        if self.estado == "Utilizada":
            raise EntradaYaUtilizada()  # no se toca la hora de ingreso original
        if self.estado != "Emitida":
            raise TicketNoEmitido()
        self.hora_ingreso = datetime.now()
        self.estado = "Utilizada"