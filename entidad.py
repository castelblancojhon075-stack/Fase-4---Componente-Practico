from abc import ABC, abstractmethod

# Clase abstracta principal del sistema

class Entidad(ABC):

    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @abstractmethod
    def mostrar_info(self):
        pass