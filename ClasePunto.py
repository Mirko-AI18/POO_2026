# ==========================================
# Clase Punto
# Representa una coordenada en el plano (X,Y)
# ==========================================

class Punto:

    # Constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Setters
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    # Método que devuelve el punto en formato texto
    def __str__(self):
        return f"({self.x}, {self.y})"
