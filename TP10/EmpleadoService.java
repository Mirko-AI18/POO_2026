
import java.util.ArrayList;
import java.util.List;

public class EmpleadoService {

    private static List<Empleado> empleados = new ArrayList<>();
    private static int proximoLegajo = 1;

    public static Boolean agregar(Empleado empleado)
            throws EnteroPositivoException {

        empleado.setLegajo(proximoLegajo++);
        return empleados.add(empleado);
    }

    public static Empleado mayorSueldo()
            throws CollectionVaciaException {

        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }

        Empleado mayor = empleados.get(0);

        for (Empleado empleado : empleados) {
            if (empleado.getSueldo() > mayor.getSueldo()) {
                mayor = empleado;
            }
        }

        return mayor;
    }

    public static Double sueldoPromedio()
            throws CollectionVaciaException {

        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }

        int suma = 0;

        for (Empleado empleado : empleados) {
            suma += empleado.getSueldo();
        }

        return (double) suma / empleados.size();
    }

    public static void eliminar(String nombre)
            throws CollectionVaciaException, NoEncontradoException {

        if (empleados.isEmpty()) {
            throw new CollectionVaciaException("No hay empleados.");
        }

        boolean eliminado = empleados.removeIf(
                e -> e.getNombre().equals(nombre));

        if (!eliminado) {
            throw new NoEncontradoException(
                    "No se encontro el empleado.");
        }
    }
}
