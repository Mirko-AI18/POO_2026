import java.util.HashMap;
import java.util.Map;

public class CatalogoProductos {
    private Map<String, Producto> baseDeDatos;

    public CatalogoProductos() {
        this.baseDeDatos = new HashMap<>();
        // El catálogo instancia los productos disponibles
        baseDeDatos.put("P1", new Producto("Leche", 1200.0, 0.0));
        baseDeDatos.put("P2", new Producto("Detergente", 2500.0, 0.21));
    }

    public Producto buscarProducto(String codigo) {
        return baseDeDatos.get(codigo);
    }
}