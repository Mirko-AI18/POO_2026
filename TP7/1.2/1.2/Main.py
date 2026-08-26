from Factura import Factura
from CalculadoraFacturacion import CalculadoraFacturacion
from FacturaDAO import FacturaDAO
from ImpresorFactura import ImpresorFactura

def main():
    factura = Factura("Juan Pérez", 1000, "VIP")

    calculadora = CalculadoraFacturacion()
    calculadora.calcular_total(factura)

    dao = FacturaDAO()
    dao.guardar(factura)

    impresor = ImpresorFactura()
    impresor.imprimir(factura)


if __name__ == "__main__":
    main()