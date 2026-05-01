class SoftwareFJError(Exception):
    """
    Clase base.Sirve para agrupar todos nuestros errores bajo un mismo nombre. 
    Es útil si queremos atrapar 'cualquier error que nosotros hayamos inventado'.
    """
    pass

class DatoInvalidoError(SoftwareFJError):
    """
    Utilidad: Se lanza cuando el usuario escribe números negativos o 
    deja campos vacíos. Evita que los cálculos matemáticos den resultados absurdos.
    """
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """
    Utilidad: Útil para cuando un cliente intenta reservar una sala o equipo 
    que ya está ocupado o no existe en el catálogo.
    """
    pass
