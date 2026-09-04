public class LineaFactura {
    private int cantidad;
    private Producto producto;
    private double precioBaseHistorico;
    private double porcentajeIvaHistorico;

    public LineaFactura(int cantidad, Producto producto) {
        this.cantidad = cantidad;
        this.producto = producto;
        // Se guardan los atributos históricos en el momento de la creación
        this.precioBaseHistorico = producto.getPrecioBase();
        this.porcentajeIvaHistorico = producto.getPorcentajeIva();
    }
    
    // Métodos que cumplen Ley de Demeter calculando sus propios subtotales
    public double getSubtotalNeto() {
        return cantidad * precioBaseHistorico;
    }
}