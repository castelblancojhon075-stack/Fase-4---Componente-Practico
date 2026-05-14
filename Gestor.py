import logging

# Configuración del archivo de logs

import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GestorSistema:

    def __init__(self):

        # Lista de clientes
        self.clientes = []

        # Lista de servicios
        self.servicios = []

        # Lista de reservas
        self.reservas = []

    # Registrar clientes
    def agregar_cliente(self, cliente):

        self.clientes.append(cliente)

        logging.info(
            f"Cliente agregado correctamente: {cliente.nombre}"
        )

    # Registrar servicios
    def agregar_servicio(self, servicio):

        self.servicios.append(servicio)

        logging.info(
            f"Servicio agregado: {servicio.nombre}"
        )

    # Registrar reservas
    def agregar_reserva(self, reserva):

        self.reservas.append(reserva)

        logging.info(
            f"Reserva registrada para: {reserva.cliente.nombre}"
        )

    # Registrar errores
    def registrar_error(self, error):

        logging.error(error)