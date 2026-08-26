from abc import ABC, abstractmethod


class correo(ABC):

    @abstractmethod
    def obtener_costo(self, peso):
        pass


class oca(correo):

    def obtener_costo(self, peso):
        return peso * 100


class fedex(correo):

    def obtener_costo(self, peso):
        return peso * 150


class andreani(correo):

    def obtener_costo(self, peso):
        return peso * 120


class calculadoraEnvios:

    def calcular(self, correo, peso):
        return correo.obtener_costo(peso)


# ejemplo de contratacion de DHL

class DHL(correo):

    def obtener_costo(self, peso):
        return peso * 180