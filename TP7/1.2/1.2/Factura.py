class Factura:
    def __init__(self, nombre_cliente, monto_base, tipo_cliente):
        self.nombre_cliente = nombre_cliente
        self.monto_base = monto_base
        self.tipo_cliente = tipo_cliente
        self.total_final = 0.0