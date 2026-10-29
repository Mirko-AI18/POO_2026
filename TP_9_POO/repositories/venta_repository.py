from sqlalchemy.orm import Session

from models import Venta


class VentaRepository:
    """Acceso a datos de Ventas."""

    def __init__(self, db: Session):
        self.db = db

    def guardar(self, venta: Venta) -> Venta:
        """Guarda la venta y los cambios de sus entradas en una sola transacción."""
        self.db.add(venta)
        self.db.commit()
        self.db.refresh(venta)
        return venta