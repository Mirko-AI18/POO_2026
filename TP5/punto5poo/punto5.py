import math
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Clase Auxiliar
# ---------------------------------------------------------
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


# ---------------------------------------------------------
# 5. Superclase Abstracta (Arquitectura Abstracta)
# ---------------------------------------------------------
class ElementoGrafico(ABC):
    def __init__(self, color_hex: str, posicion_centro: Punto, nombre_capa: str):
        self.color_hex = color_hex
        self.posicion_centro = posicion_centro
        self.nombre_capa = nombre_capa

    def mover_a(self, nuevo_destino: Punto) -> None:
        self.posicion_centro = nuevo_destino

    @abstractmethod
    def calcular_area(self) -> float:
        """Contrato obligatorio para subclases."""
        pass

    @abstractmethod
    def calcular_perimetro(self) -> float:
        """Contrato obligatorio para subclases."""
        pass

    @abstractmethod
    def escalar(self, factor: float) -> None:
        """Contrato obligatorio para subclases."""
        pass

    def __str__(self) -> str:
        return f"[{self.nombre_capa}] Color: {self.color_hex} | Pos: {self.posicion_centro}"


# ---------------------------------------------------------
# Subclases Concretas
# ---------------------------------------------------------
class Rectangulo(ElementoGrafico):
    def __init__(self, color_hex: str, posicion_centro: Punto, nombre_capa: str, lado_menor: float, lado_mayor: float):
        super().__init__(color_hex, posicion_centro, nombre_capa)
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor

    def calcular_area(self) -> float:
        return self.lado_menor * self.lado_mayor

    def calcular_perimetro(self) -> float:
        return 2 * (self.lado_menor + self.lado_mayor)

    def escalar(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("El factor de escala debe ser mayor a 0.")
        self.lado_menor *= factor
        self.lado_mayor *= factor

    def __str__(self) -> str:
        return f"{super().__str__()} | Rectángulo ({self.lado_menor}x{self.lado_mayor})"


class Elipse(ElementoGrafico):
    def __init__(self, color_hex: str, posicion_centro: Punto, nombre_capa: str, radio_menor: float, radio_mayor: float):
        super().__init__(color_hex, posicion_centro, nombre_capa)
        self.radio_menor = radio_menor
        self.radio_mayor = radio_mayor

    def calcular_area(self) -> float:
        return math.pi * self.radio_menor * self.radio_mayor

    def calcular_perimetro(self) -> float:
        a, b = self.radio_mayor, self.radio_menor
        return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

    def escalar(self, factor: float) -> None:
        if factor <= 0:
            raise ValueError("El factor de escala debe ser mayor a 0.")
        self.radio_menor *= factor
        self.radio_mayor *= factor

    def __str__(self) -> str:
        return f"{super().__str__()} | Elipse (r={self.radio_menor}, R={self.radio_mayor})"


class Cuadrado(Rectangulo):
    def __init__(self, color_hex: str, posicion_centro: Punto, nombre_capa: str, lado: float):
        super().__init__(color_hex, posicion_centro, nombre_capa, lado, lado)


class Circulo(Elipse):
    def __init__(self, color_hex: str, posicion_centro: Punto, nombre_capa: str, radio: float):
        super().__init__(color_hex, posicion_centro, nombre_capa, radio, radio)


# ---------------------------------------------------------
# Motor de Renderizado y Bucle Polimórfico (Lienzo)
# ---------------------------------------------------------
class Lienzo:
    def __init__(self):
        self.elementos: list[ElementoGrafico] = []

    def agregar_elemento(self, elem: ElementoGrafico) -> None:
        self.elementos.append(elem)

    def procesar_elementos(self) -> float:
        area_total = 0.0
        origen = Punto(0, 0)

        for elem in self.elementos:
            # 1. Filtro escala de grises
            elem.color_hex = "#808080"
            # 2. Mover a punto (0,0)
            elem.mover_a(origen)
            # 3. Sumar área de forma polimórfica
            area_total += elem.calcular_area()

        return area_total


# ---------------------------------------------------------
# Ejecución (Main)
# ---------------------------------------------------------
if __name__ == "__main__":
    canvas = Lienzo()

    # Instanciación de formas
    canvas.agregar_elemento(Rectangulo("#FF0000", Punto(10, 20), "Capa_Rect", 4.0, 5.0))
    canvas.agregar_elemento(Elipse("#00FF00", Punto(5, 5), "Capa_Elipse", 2.0, 3.0))
    canvas.agregar_elemento(Cuadrado("#0000FF", Punto(-2, 4), "Capa_Cuadrado", 3.0))
    canvas.agregar_elemento(Circulo("#FFFF00", Punto(1, 1), "Capa_Circulo", 2.0))

    # Bucle polimórfico
    total_area = canvas.procesar_elementos()

    # Resultados por consola
    print("--- ELEMENTOS PROCESADOS EN EL LIENZO ---")
    for elem in canvas.elementos:
        print(elem)

    print(f"\nÁrea total ocupada por los elementos: {total_area:.2f} px")