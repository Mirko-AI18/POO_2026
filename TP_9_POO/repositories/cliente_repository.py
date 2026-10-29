from sqlalchemy.orm import Session

from models import Cliente


class ClienteRepository:
    """Acceso a datos de Clientes."""

    def __init__(self, db: Session):
        self.db = db

    def obtener(self, cliente_id: int) -> Cliente | None:
        return self.db.get(Cliente, cliente_id)