from entidad import Entidad
from excepciones import ClienteInvalidoError

# Clase Cliente con encapsulación y validaciones

class Cliente(Entidad):

    # Constructor de la clase cliente
    def __init__(self, id_cliente, nombre, correo):

        # Llamado al constructor padre
        super().__init__(id_cliente)

        # Validación del nombre
        if len(nombre.strip()) < 3:
            raise ClienteInvalidoError(
                "El nombre del cliente es inválido."
            )

        # Validación del correo
        if "@" not in correo:
            raise ClienteInvalidoError(
                "El correo electrónico no es válido."
            )

        # Encapsulación de atributos
        self.__nombre = nombre
        self.__correo = correo