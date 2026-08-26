class FacturaDAO:
    def guardar(self, factura):
        try:
            conexion = sqlite3.connect("mi_empresa.db")
            cursor = conexion.cursor()

            query = f"INSERT INTO facturas (cliente, total) VALUES ('{factura.nombre_cliente}', {factura.total_final})"

            cursor.execute(query)
            conexion.commit()
            conexion.close()

        except Exception as e:
            print(f"Error bd: {e}")