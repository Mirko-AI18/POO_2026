# ==========================================
# Clase Rectangulo
# Hereda de ElementoGrafico
# ==========================================

class Rectangulo(ElementoGrafico):

    # Constructor
    def __init__(self, color_hex, posicion_centro, nombre_capa,
                 lado_menor, lado_mayor):

        # Llama al constructor de la clase padre
        super().__init__(color_hex, posicion_centro, nombre_capa)

        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor

    # Getters
    def get_lado_menor(self):
        return self.lado_menor

    def get_lado_mayor(self):
        return self.lado_mayor

    # Setters
    def set_lado_menor(self, lado_menor):
        self.lado_menor = lado_menor

    def set_lado_mayor(self, lado_mayor):
        self.lado_mayor = lado_mayor

    # Área = base × altura
    def calcularArea(self):
        return self.lado_menor * self.lado_mayor

    # Perímetro = 2(base + altura)
    def calcularPerimetro(self):
        return 2 * (self.lado_menor + self.lado_mayor)

    # Escala los lados por un factor
    def escalar(self, factor):

        # Conceptualmente un factor <= 0
        # produciría un rectángulo inválido.
        # En una aplicación real podría lanzarse
        # una excepción o mostrar un error.

        if factor > 0:
            self.lado_menor *= factor
            self.lado_mayor *= factor

    # Sobrescribe __str__ usando super()
    def __str__(self):

        return (
            super().__str__()
            + f"\nLado menor: {self.lado_menor}"
            + f"\nLado mayor: {self.lado_mayor}"
        )