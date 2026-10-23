
public class Main {

    public static void main(String[] args) {

        // 1. Probar sueldo negativo
        try {
            Empleado empleado = new Empleado("Juan", -500);
        } catch (StringException | EnteroPositivoException e) {
            System.out.println(e.getMessage());
        }

        // 2. Probar empleado inexistente
        try {
            EmpleadoService.agregar(new Empleado("Ana", 300000));
            EmpleadoService.eliminar("Pedro");
        } catch (StringException | EnteroPositivoException | CollectionVaciaException | NoEncontradoException e) {
            System.out.println(e.getMessage());
        }

        // 3. Probar sueldo promedio de una lista vacía
        try {
            EmpleadoService.eliminar("Ana");
            EmpleadoService.sueldoPromedio();
        } catch (CollectionVaciaException | NoEncontradoException e) {
            System.out.println(e.getMessage());
        }
    }
}
