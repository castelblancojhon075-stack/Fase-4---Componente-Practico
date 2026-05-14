from entidad import Entidad
from excepciones import ClienteInvalidoError

# Clase Cliente con encapsulación y validaciones

class Cliente(Entidad):

    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)

        if len(nombre.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre del cliente es inválido."
            )

        if "@" not in correo:
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__correo}"