from edificio import Edificio
from auto import Auto
from bicicleta import Bicicleta

objetos = []

objetos.append(Edificio("Torre Central", 15000))
objetos.append(Auto("Toyota Corolla", 12000, 7))
objetos.append(Bicicleta("Mountain Bike", 3000))

print("=== IMPACTO ECOLÓGICO ===\n")

for obj in objetos:
    print(obj)
    print("Impacto ecológico:", obj.obtener_impacto_ecologico(), "kg CO2/año")
    print("-" * 40)