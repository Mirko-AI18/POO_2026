from impacto_ecologico import ImpactoEcologico

class Auto(ImpactoEcologico):

    def __init__(self, marca, km_anuales, consumo_litro_100km):
        self.marca = marca
        self.km_anuales = km_anuales
        self.consumo_litro_100km = consumo_litro_100km

    def obtener_impacto_ecologico(self):
        litros_consumidos = (self.km_anuales / 100) * self.consumo_litro_100km
        return litros_consumidos * 2.31

    def __str__(self):
        return f"Auto: {self.marca}"