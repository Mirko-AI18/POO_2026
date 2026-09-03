public class LineaFactura {
    private int cantidad;
    private Producto producto;
    private double precioUnitarioHistorico;
    private double porcentajeIvaHistorico;   
    private List<Descuento> descuentos = new ArrayList<>();

    public LineaFactura(int cantidad, Producto producto,
                         double precioUnitarioHistorico, double porcentajeIvaHistorico) {
        this.cantidad = cantidad;
        this.producto = producto;
        this.precioUnitarioHistorico = precioUnitarioHistorico;
        this.porcentajeIvaHistorico = porcentajeIvaHistorico;
    }

    public void agregarDescuento(Descuento descuento) {
        descuentos.add(descuento);
    }

    public double getNetoBruto() {
        return cantidad * precioUnitarioHistorico;
    }

    public double getMontoDescuento() {
        double montoRestante = getNetoBruto();
        double totalDescontado = 0.0;
        for (Descuento descuento : descuentos) {
            if (descuento.esAplicable(montoRestante, cantidad)) {
                double descontadoAhora = descuento.calcularMontoDescuento(montoRestante, cantidad);
                totalDescontado += descontadoAhora;
                montoRestante -= descontadoAhora;
            }
        }
        return totalDescontado;
    }

    public double getNetoImponible() {
        return getNetoBruto() - getMontoDescuento();
    }

    public double getIva() {
        return getNetoImponible() * porcentajeIvaHistorico;
    }

    public double getTotalLinea() {
        return getNetoImponible() + getIva();
    }

    public int getCantidad() { return cantidad; }
    public Producto getProducto() { return producto; }
}

public class Factura {
    private String tipoComprobante;
    private List<LineaFactura> lineas;
    private List<Descuento> descuentosFactura = new ArrayList<>();

    public Factura(String tipoComprobante, List<LineaFactura> lineas) {
        this.tipoComprobante = tipoComprobante;
        this.lineas = lineas;
    }

    public void agregarDescuentoFactura(Descuento descuento) {
        descuentosFactura.add(descuento);
    }

    private double getSubtotalSinDescuentosDeFactura() {
        double subtotal = 0.0;
        for (LineaFactura linea : lineas) {
            subtotal += linea.getNetoBruto();
        }
        return subtotal;
    }

    private int getCantidadTotalItems() {
        int total = 0;
        for (LineaFactura linea : lineas) {
            total += linea.getCantidad();
        }
        return total;
    }

    public void aplicarDescuentosDeFactura() {
        double subtotal = getSubtotalSinDescuentosDeFactura();
        int cantidadTotal = getCantidadTotalItems();
        for (Descuento descuento : descuentosFactura) {
            if (descuento.esAplicable(subtotal, cantidadTotal)) {
                for (LineaFactura linea : lineas) {
                    linea.agregarDescuento(descuento);
                }
            }
        }
    }

    public double getTotalIva() {
        double total = 0.0;
        for (LineaFactura linea : lineas) total += linea.getIva();
        return total;
    }

    public double getTotalFinal() {
        double total = 0.0;
        for (LineaFactura linea : lineas) total += linea.getTotalLinea();
        return total;
    }

    public List<LineaFactura> getLineas() { return lineas; }
    public String getTipoComprobante() { return tipoComprobante; }
}
