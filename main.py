from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from Gestor import GestorSistema

# Inicialización del sistema

gestor = GestorSistema()

print("\n===== SOFTWARE FJ =====\n")

# OPERACIÓN 1
try:
    cliente1 = Cliente(1, "Carlos", "carlos@gmail.com")
    gestor.agregar_cliente(cliente1)
    print(cliente1.mostrar_info())

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 2 (ERROR)
try:
    cliente2 = Cliente(2, "Lu", "correo_mal")
    gestor.agregar_cliente(cliente2)

except Exception as e:
    print("Error:", e)
    gestor.registrar_error(e)

# OPERACIÓN 3
try:
    sala = ReservaSala(1, "Sala Premium", 200)
    gestor.agregar_servicio(sala)
    print(sala.mostrar_info())

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 4
try:
    equipo = AlquilerEquipo(2, "Computadores", 150)
    gestor.agregar_servicio(equipo)
    print(equipo.mostrar_info())

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 5
try:
    asesoria = Asesoria(3, "Consultoría TI", 300)
    gestor.agregar_servicio(asesoria)
    print(asesoria.mostrar_info())

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 6 (ERROR)
try:
    servicio_error = ReservaSala(4, "Sala Básica", -10)

except Exception as e:
    print("Error:", e)
    gestor.registrar_error(e)

# OPERACIÓN 7
try:
    reserva1 = Reserva(cliente1, sala, 5)
    gestor.agregar_reserva(reserva1)

    total = reserva1.procesar_reserva()

    print("Reserva procesada.")
    print("Costo total:", total)
    print("Estado:", reserva1.estado)

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 8
try:
    reserva2 = Reserva(cliente1, equipo, 2)
    gestor.agregar_reserva(reserva2)

    total = reserva2.procesar_reserva()

    print("Costo total:", total)

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 9
try:
    reserva3 = Reserva(cliente1, asesoria, 3)
    gestor.agregar_reserva(reserva3)

    total = reserva3.procesar_reserva()

    print("Costo total:", total)

except Exception as e:
    gestor.registrar_error(e)

# OPERACIÓN 10 (ERROR)
try:
    reserva_error = Reserva(cliente1, sala, -4)

except Exception as e:
    print("Error:", e)
    gestor.registrar_error(e)

print("\nSistema ejecutado correctamente.")