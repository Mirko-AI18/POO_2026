# ==========================================
# Clase ElementoGrafico
# Superclase para cualquier objeto visual
# ==========================================

class ElementoGrafico:

    # Constructor
    def __init__(self, color_hex, posicion_centro, nombre_capa):
        self.color_hex = color_hex
        self.posicion_centro = posicion_centro
        self.nombre_capa = nombre_capa

    # -------------------------
    # Getters
    # -------------------------

    def get_color_hex(self):
        return self.color_hex

    def get_posicion_centro(self):
        return self.posicion_centro

    def get_nombre_capa(self):
        return self.nombre_capa

    # -------------------------
    # Setters
    # -------------------------

    def set_color_hex(self, color_hex):
        self.color_hex = color_hex

    def set_posicion_centro(self, posicion_centro):
        self.posicion_centro = posicion_centro

    def set_nombre_capa(self, nombre_capa):
        self.nombre_capa = nombre_capa

    # --------------------------------------
    # moverA()
    # Cambia la posición central del objeto
    # --------------------------------------

    def moverA(self, nuevo_destino):
        self.posicion_centro = nuevo_destino

    # --------------------------------------
    # toString()
    # En Python se sobrescribe mediante __str__
    # --------------------------------------

    def __str__(self):
        return (
            f"ElementoGrafico\n"
            f"Color: {self.color_hex}\n"
            f"Centro: {self.posicion_centro}\n"
            f"Capa: {self.nombre_capa}"
        )
