from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from database import Base, engine
import models  # noqa: F401  (registra las tablas)
from exceptions import DominioError
from routers import (
    cotizar, pagos, acceso, lugares, sectores, clientes, eventos
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartTicket API",
    description="Gestión de eventos y control de accesos",
    version="0.1.0",
)


@app.exception_handler(DominioError)
def manejar_error_de_dominio(request: Request, exc: DominioError):
    """Traduce los errores de negocio a respuestas HTTP (así el controlador no tiene ifs)."""
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.mensaje})


app.include_router(lugares.router)
app.include_router(sectores.router)
app.include_router(clientes.router)
app.include_router(eventos.router)
app.include_router(cotizar.router)
app.include_router(pagos.router)
app.include_router(acceso.router)