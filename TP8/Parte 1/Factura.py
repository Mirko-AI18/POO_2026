class Factura:

    def __init__(self, tipo_comprobante, porcentaje_descuento, lineas):
        self.tipo_comprobante = tipo_comprobante
        self.porcentaje_descuento = porcentaje_descuento
        self.lineas = lineas

    def imprimir_factura(self):

        total_neto = 0.0
        total_iva = 0.0
        total_final = 0.0

        for linea in self.lineas:
            # Ahora usamos el precio histórico guardado
            # en la línea de factura.
            neto_linea = linea.cantidad * linea.precio_unitario

            # Ahora usamos el IVA histórico guardado
            # en la línea de factura.
            iva_linea = neto_linea * linea.porcentaje_iva

            if self.tipo_comprobante == "A":
                total_neto += neto_linea
                total_iva += iva_linea
                total_final += (neto_linea + iva_linea)

            elif self.tipo_comprobante == "B":
                total_final += (neto_linea + iva_linea)

        if self.tipo_comprobante == "B":
            monto_descuento = total_final * self.porcentaje_descuento
            total_final = total_final - monto_descuento

        print(f"Total a Pagar: ${total_final}")

        if self.tipo_comprobante == "A":
            print(f"Detalle IVA: ${total_iva}")