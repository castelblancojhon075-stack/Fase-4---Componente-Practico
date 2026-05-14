from abc import ABC, abstractmethod
# Clase abstracta principal del sistema

class Entidad(ABC):

    # Constructor principal
    def __init__(self, id_entidad):

        # Atributo protegido
        self._id_entidad = id_entidad

    # Método abstracto obligatorio
    @abstractmethod
    def mostrar_info(self):
        pass