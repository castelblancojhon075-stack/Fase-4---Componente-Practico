from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import ServicioNoDisponibleError

# Clase abstracta Servicio

class Servicio(Entidad, ABC):

    def __init__(self, id_servicio, nombre, tarifa_base):
        super().__init__(id_servicio)

        if tarifa_base <= 0:
            raise ServicioNoDisponibleError(
                "La tarifa debe ser mayor que cero."
            )

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        total = self.tarifa_base * horas

        total += total * impuesto
        total -= descuento

        return total

    def mostrar_info(self):
        return f"Servicio Sala: {self.nombre}"


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        total = (self.tarifa_base * horas) + 50

        total += total * impuesto
        total -= descuento

        return total

    def mostrar_info(self):
        return f"Servicio Equipo: {self.nombre}"


# Servicio de asesorías
class Asesoria(Servicio):

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        total = (self.tarifa_base * horas) + 100

        total += total * impuesto
        total -= descuento

        return total

    def mostrar_info(self):
        return f"Servicio Asesoría: {self.nombre}"