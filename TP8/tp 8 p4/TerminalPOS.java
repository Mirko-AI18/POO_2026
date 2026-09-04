public class TerminalPOS {
    private Factura facturaActual;
    private CatalogoProductos catalogo;

    public TerminalPOS(CatalogoProductos catalogo) {
        this.catalogo = catalogo;
    }

    public void iniciarVenta(String tipoComprobante) {
        // La terminal instancia la Factura
        this.facturaActual = new Factura(tipoComprobante);
    }

    public void escanearProducto(String codigo, int cantidad) {
        Producto prod = catalogo.buscarProducto(codigo);
        if (prod != null && facturaActual != null) {
            // Se le pide a la Factura que agregue la línea (Ella la creará)
            facturaActual.agregarLinea(cantidad, prod);
        }
    }
}

