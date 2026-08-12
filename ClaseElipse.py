import math

# ==========================================
# Clase Elipse
# Hereda de ElementoGrafico
# ==========================================

class Elipse(ElementoGrafico):

    # Constructor
    def __init__(self, color_hex, posicion_centro, nombre_capa,
                 radio_mayor, radio_menor):

        super().__init__(color_hex, posicion_centro, nombre_capa)

        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor

    # Getters
    def get_radio_mayor(self):
        return self.radio_mayor

    def get_radio_menor(self):
        return self.radio_menor

    # Setters
    def set_radio_mayor(self, radio_mayor):
        self.radio_mayor = radio_mayor

    def set_radio_menor(self, radio_menor):
        self.radio_menor = radio_menor

    # Área = π × R × r
    def calcularArea(self):
        return math.pi * self.radio_mayor * self.radio_menor

    # Aproximación de Ramanujan para el perímetro
    def calcularPerimetro(self):

        R = self.radio_mayor
        r = self.radio_menor

        return math.pi * (3 * (R + r) - math.sqrt((3 * R + r) * (R + 3 * r)))

    # Escala ambos radios
    def escalar(self, factor):

        # Si factor es 0 o negativo
        # la elipse dejaría de existir.
        # En una aplicación real debería
        # rechazarse el valor.

        if factor > 0:
            self.radio_mayor *= factor
            self.radio_menor *= factor

    # Sobrescribe __str__ usando super()
    def __str__(self):

        return (
            super().__str__()
            + f"\nRadio mayor: {self.radio_mayor}"
            + f"\nRadio menor: {self.radio_menor}"
        )