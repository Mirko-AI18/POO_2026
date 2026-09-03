public interface Descuento {
    boolean esAplicable(double montoBase, int cantidad);
    double calcularMontoDescuento(double montoBase, int cantidad);
    String getDescripcion();
}

public class DescuentoTresPorDos implements Descuento {

    @Override
    public boolean esAplicable(double montoBase, int cantidad) {
        return cantidad >= 3;
    }

    @Override
    public double calcularMontoDescuento(double montoBase, int cantidad) {
        double precioUnitario = montoBase / cantidad;
        int unidadesGratis = cantidad / 3; 
        return unidadesGratis * precioUnitario;
    }

    @Override
    public String getDescripcion() {
        return "Promoción 3x2";
    }
}

public class DescuentoPorVolumen implements Descuento {
    private final double montoMinimo;
    private final double porcentaje;

    public DescuentoPorVolumen(double montoMinimo, double porcentaje) {
        this.montoMinimo = montoMinimo;
        this.porcentaje = porcentaje;
    }

    @Override
    public boolean esAplicable(double montoBase, int cantidad) {
        return montoBase >= montoMinimo;
    }

    @Override
    public double calcularMontoDescuento(double montoBase, int cantidad) {
        return montoBase * porcentaje;
    }

    @Override
    public String getDescripcion() {
        return "Descuento por volumen (compra >= $" + montoMinimo + ")";
    }
}

public class DescuentoPorCategoria implements Descuento {
    private final String categoriaCliente;
    private final double porcentaje;

    public DescuentoPorCategoria(String categoriaCliente, double porcentaje) {
        this.categoriaCliente = categoriaCliente;
        this.porcentaje = porcentaje;
    }

    @Override
    public boolean esAplicable(double montoBase, int cantidad) {
        return montoBase > 0;
    }

    @Override
    public double calcularMontoDescuento(double montoBase, int cantidad) {
        return montoBase * porcentaje;
    }

    @Override
    public String getDescripcion() {
        return "Descuento por categoría: " + categoriaCliente;
    }
}
