from sqlalchemy.orm import Session

from models import PrecioSector


class PrecioSectorRepository:
    """Acceso a datos de los precios por sector de cada evento."""

    def __init__(self, db: Session):
        self.db = db

    def obtener(self, evento_id: int, sector_id: int) -> PrecioSector | None:
        return (
            self.db.query(PrecioSector)
            .filter(
                PrecioSector.evento_id == evento_id,
                PrecioSector.sector_id == sector_id,
            )
            .first()
        )