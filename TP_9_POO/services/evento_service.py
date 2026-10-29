import uuid

from sqlalchemy.orm import Session

from models import Evento, PrecioSector, Entrada, Lugar
import schemas


class EventoService:
    """Reglas de negocio para crear un Evento."""

    def __init__(self, db: Session):
        self.db = db

    def crear_evento(self, datos: schemas.EventoCreate) -> Evento:
        lugar = self.db.get(Lugar, datos.lugar_id)
        if lugar is None:
            raise LookupError("Lugar no encontrado")

        sectores = {s.id: s for s in lugar.sectores}
        ids_precios = [p.sector_id for p in datos.precios]

        if len(ids_precios) != len(set(ids_precios)):
            raise ValueError("Hay sectores repetidos en la lista de precios")
        if set(ids_precios) != set(sectores):
            raise ValueError(
                "Hay que definir el precio de todos los sectores del lugar "
                "(y solo de ellos)"
            )

        evento = Evento(nombre=datos.nombre, fecha=datos.fecha, lugar_id=lugar.id)
        self.db.add(evento)
        self.db.flush()  # obtiene el id del evento

        for p in datos.precios:
            self.db.add(PrecioSector(
                evento_id=evento.id, sector_id=p.sector_id, precio=p.precio
            ))

        # Las entradas se generan según la capacidad de cada sector
        for sector in sectores.values():
            for _ in range(sector.capacidad_maxima):
                self.db.add(Entrada(
                    estado="Disponible",
                    codigo_qr=str(uuid.uuid4()),
                    evento_id=evento.id,
                    sector_id=sector.id,
                ))

        self.db.commit()  # todo o nada
        self.db.refresh(evento)
        return evento