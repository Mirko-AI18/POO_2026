from impacto_ecologico import ImpactoEcologico

class Edificio(ImpactoEcologico):

    def __init__(self, nombre, consumo_kwh_anual):
        self.nombre = nombre
        self.consumo_kwh_anual = consumo_kwh_anual

    def obtener_impacto_ecologico(self):
        return self.consumo_kwh_anual * 0.4

    def __str__(self):
        return f"Edificio: {self.nombre}"