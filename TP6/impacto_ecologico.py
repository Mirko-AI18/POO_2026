from abc import ABC, abstractmethod

class ImpactoEcologico(ABC):

    @abstractmethod
    def obtener_impacto_ecologico(self):
        pass