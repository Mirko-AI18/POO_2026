from impacto_ecologico import ImpactoEcologico

class Bicicleta(ImpactoEcologico):

    def __init__(self, modelo, km_anuales):
        self.modelo = modelo
        self.km_anuales = km_anuales

    def obtener_impacto_ecologico(self):
        return 0

    def __str__(self):
        return f"Bicicleta: {self.modelo}"