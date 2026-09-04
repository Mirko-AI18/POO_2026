class LineaFactura:

    def __init__(self, producto, cantidad):

        self.producto = producto
        self.cantidad = cantidad

        # Guardamos el precio del producto al momento
        # de realizar la venta.
        self.precio_unitario = producto.precio_base

        # Guardamos el IVA vigente al momento
        # de realizar la venta.
        self.porcentaje_iva = producto.porcentaje_iva