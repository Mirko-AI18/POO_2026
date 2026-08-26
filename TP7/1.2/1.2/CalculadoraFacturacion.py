class CalculadoraFacturacion:
    def calcular_total(self, factura):
        descuento = 0.0
        DESCUENTO_VIP = 0.20
        DESCUENTO_REGULAR = 0.10

        if factura.tipo_cliente == "VIP":
            descuento = factura.monto_base * DESCUENTO_VIP
        elif factura.tipo_cliente == "REGULAR":
            descuento = factura.monto_base * DESCUENTO_REGULAR

factura.total_final = factura.monto_base - descuento