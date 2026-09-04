import java.util.ArrayList;
import java.util.List;

public class Factura {
    private String tipoComprobante;
    private List<LineaFactura> lineas;

    public Factura(String tipoComprobante) {
        this.tipoComprobante = tipoComprobante;
        this.lineas = new ArrayList<>();
    }

    public void agregarLinea(int cantidad, Producto producto) {
        // Patrón Creador: Factura instancia la LineaFactura
        LineaFactura nuevaLinea = new LineaFactura(cantidad, producto);
        this.lineas.add(nuevaLinea);
    }
}
