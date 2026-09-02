import java.util.List;
import java.util.ArrayList;

// 1. Clase Producto
class Producto {
    private String nombre;
    private double precioBase;
    private double porcentajeIva;

    public Producto(String nombre, double precioBase, double porcentajeIva) {
        this.nombre = nombre;
        this.precioBase = precioBase;
        this.porcentajeIva = porcentajeIva;
    }

    public double getPrecioBase() {
        return precioBase;
    }

    public double getPorcentajeIva() {
        return porcentajeIva;
    }

    public String getNombre() {
        return nombre;
    }
}

// 2. Clase LineaFactura (Aplica descuento linea por linea antes de calcular IVA)
class LineaFactura {
    private int cantidad;
    private Producto producto;

    public LineaFactura(int cantidad, Producto producto) {
        this.cantidad = cantidad;
        this.producto = producto;
    }

    public int getCantidad() {
        return cantidad;
    }

    public Producto getProducto() {
        return producto;
    }

    // Calcula el subtotal neto aplicando el descuento 
    public double getNetoLinea(double porcentajeDescuento) {
        double subtotal = cantidad * producto.getPrecioBase();
        return subtotal - (subtotal * porcentajeDescuento);
    }

    // Calcula el IVA sobre el neto rebajado
    public double getIvaLinea(double porcentajeDescuento) {
        return getNetoLinea(porcentajeDescuento) * producto.getPorcentajeIva();
    }
}

// 3. Clase Factura (suma totales)
class Factura {
    private String tipoComprobante; // "A" o "B"
    private double porcentajeDescuento; // Ej: 0.15 para 15%
    private List<LineaFactura> lineas;

    public Factura(String tipoComprobante, double porcentajeDescuento, List<LineaFactura> lineas) {
        this.tipoComprobante = tipoComprobante;
        this.porcentajeDescuento = porcentajeDescuento;
        this.lineas = lineas;
    }

    public String getTipoComprobante() {
        return tipoComprobante;
    }

    // Suma del neto total con descuento
    public double getTotalNeto() {
        double total = 0;
        for (LineaFactura l : lineas) {
            total += l.getNetoLinea(porcentajeDescuento);
        }
        return total;
    }

    // Suma de IVA  (21% o 10.5%)
    public double getIvaPorAlicuota(double alicuota) {
        double totalIva = 0;
        for (LineaFactura l : lineas) {
            if (l.getProducto().getPorcentajeIva() == alicuota) {
                totalIva += l.getIvaLinea(porcentajeDescuento);
            }
        }
        return totalIva;
    }

    // Suma de todo el IVA
    public double getTotalIva() {
        double totalIva = 0;
        for (LineaFactura l : lineas) {
            totalIva += l.getIvaLinea(porcentajeDescuento);
        }
        return totalIva;
    }

    // Total a pagar
    public double getTotalFinal() {
        return getTotalNeto() + getTotalIva();
    }
}

// 4. Fabricacion Pura (imprime todo)
class ImpresorFacturaConsola {

    public static void imprimir(Factura factura) {
        System.out.println("FACTURA TIPO " + factura.getTipoComprobante());
        System.out.println("Subtotal Neto: $" + factura.getTotalNeto());
        System.out.println("Detalle IVA");
        System.out.println("IVA 21%: $" + factura.getIvaPorAlicuota(0.21));
        System.out.println("IVA 10.5%: $" + factura.getIvaPorAlicuota(0.105));
        System.out.println("Total IVA: $" + factura.getTotalIva());
        System.out.println("");
        System.out.println("TOTAL FINAL: $" + factura.getTotalFinal());
    }
}