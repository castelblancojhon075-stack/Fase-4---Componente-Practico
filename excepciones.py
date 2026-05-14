# Archivo que contiene las excepciones personalizadas del sistema

class ErrorSistema(Exception):
    """Excepción base del sistema"""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error para clientes inválidos"""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando un servicio no está disponible"""
    pass


class ReservaError(ErrorSistema):
    """Error relacionado con reservas"""
    pass