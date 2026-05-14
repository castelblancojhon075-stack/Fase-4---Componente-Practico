from excepciones import ReservaError

# Clase Reserva

class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ReservaError(
                "La duración de la reserva es inválida."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):

        try:
            costo = self.servicio.calcular_costo(
                self.horas,
                impuesto=0.19,
                descuento=20
            )

        except Exception as error:
            raise ReservaError(
                "Error al procesar la reserva."
            ) from error

        else:
            self.confirmar()
            return costo

        finally:
            print("Proceso de reserva finalizado.")