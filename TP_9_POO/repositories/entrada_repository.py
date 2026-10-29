from sqlalchemy.orm import Session

from models import Entrada


class EntradaRepository:
    """Acceso a datos de Entradas."""

    def __init__(self, db: Session):
        self.db = db

    def contar_disponibles(self, evento_id: int, sector_id: int) -> int:
        return (
            self.db.query(Entrada)
            .filter(
                Entrada.evento_id == evento_id,
                Entrada.sector_id == sector_id,
                Entrada.estado == "Disponible",
            )
            .count()
        )

    def obtener_disponibles(
        self, evento_id: int, sector_id: int, cantidad: int
    ) -> list[Entrada]:
        """Trae hasta `cantidad` entradas Disponibles de ese evento y sector."""
        return (
            self.db.query(Entrada)
            .filter(
                Entrada.evento_id == evento_id,
                Entrada.sector_id == sector_id,
                Entrada.estado == "Disponible",
            )
            .order_by(Entrada.id)
            .limit(cantidad)
            .all()
        )

    def obtener_por_qr(self, codigo_qr: str) -> Entrada | None:
        return (
            self.db.query(Entrada)
            .filter(Entrada.codigo_qr == codigo_qr)
            .first()
        )

    def guardar(self, entrada: Entrada) -> Entrada:
        self.db.add(entrada)
        self.db.commit()
        self.db.refresh(entrada)
        return entrada