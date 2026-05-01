from excepciones import DatoInvalidoError, ReservaIncorrectaError
import logging

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        """
        Esta clase va a actuar como el 'pegamento' del sistema. 
        Su utilidad es conectar a un objeto Cliente con un objeto Servicio.
        """
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar_reserva(self):
        """
        Aquí aplicamos el manejo robusto de excepciones. 
        Su utilidad es intentar realizar el cobro y, si algo falla, 
        registrarlo en el log para que el programa no se detenga.
        """
        try:
            total = self.servicio.calcular_costo(self.duracion)
            
            if total <= 0:
                raise ReservaIncorrectaError("El costo total no puede ser cero o negativo.")
            
            self.estado = "Confirmada"
            return f"Reserva Exitosa: {total:.2f}"

        except ReservaIncorrectaError as e:
            logging.error(f"Fallo en reserva para {self.cliente}: {e}")
            self.estado = "Fallida"
            raise 
            
        except Exception as e:
            logging.critical(f"Error inesperado en el sistema: {e}", exc_info=True)
            self.estado = "Error de Sistema"
            raise
