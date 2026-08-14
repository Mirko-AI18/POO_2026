from abc import ABC, abstractmethod

# 1. Base
class ElementoGrafico(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

# 2. Rectangulo
class Rectangulo(ElementoGrafico):

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

# 3. Cuadrado
class Cuadrado(ElementoGrafico):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado
    


# Crear un rectangulo 
rect = Rectangulo(5, 3)
print("--- Rectángulo ---")
print("Área:", rect.calcular_area())
print("Perímetro:", rect.calcular_perimetro())

# Crear un cuadrado 
cuad = Cuadrado(4)
print("\n--- Cuadrado ---")
print("Área:", cuad.calcular_area())
print("Perímetro:", cuad.calcular_perimetro())