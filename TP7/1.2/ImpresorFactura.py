class ImpresorFactura:
    def imprimir(self, factura):
        print(f"FACTURA: {factura.nombre_cliente} | Total: ${factura.total_final}")
