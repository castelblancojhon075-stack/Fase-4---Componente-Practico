import logging

# Configuración del archivo de logs

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Clase encargada de administrar el sistema

class GestorSistema:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def registrar_error(self, error):
        logging.error(error)