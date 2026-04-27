
"""
integrantes: deiver camilo legarda - jessica valentina chaves juardo-santiago jimenez rivera 
 fecha: 21-06-2026
 carrera: ingenieria de sistemas
 cusro:programacion orientada a objetos
 profesor: juan pablo arango cardona 
"""

import logging
import os
import re
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

# ==================== EXCEPCIONES PERSONALIZADAS ====================

class SistemaError(Exception):
    """Excepción base del sistema"""
    pass

class ClienteError(SistemaError):
    """Errores relacionados con clientes"""
    pass

class ServicioError(SistemaError):
    """Errores relacionados con servicios"""
    pass

class ReservaError(SistemaError):
    """Errores relacionados con reservas"""
    pass

class ValidacionError(SistemaError):
    """Errores de validación de datos"""
    pass

class ServicioNoDisponibleError(ServicioError):
    """Servicio no disponible en el momento"""
    pass

class ClienteNoEncontradoError(ClienteError):
    """Cliente no encontrado en el sistema"""
    pass

# ==================== SISTEMA DE LOGS ====================

class SistemaLogger:
    """Gestor de logs para el sistema (Singleton)"""
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia
    
    def _inicializar(self):
        """Inicializa la configuración del logger"""
        # Crear directorio de logs si no existe
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Configurar logging
        self.logger = logging.getLogger('SistemaFJ')
        self.logger.setLevel(logging.DEBUG)
        
        # Handler para archivo
        file_handler = logging.FileHandler('logs/sistema.log', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Formato
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
    
    def registrar_evento(self, mensaje, nivel='INFO'):
        """Registra un evento en el log"""
        niveles = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.logger.log(niveles.get(nivel, logging.INFO), mensaje)
    
    def registrar_error(self, error, contexto=""):
        """Registra un error con contexto"""
        mensaje = f"{contexto} - {str(error)}" if contexto else str(error)
        self.registrar_evento(mensaje, 'ERROR')

# ==================== CLASE ABSTRACTA ENTIDAD ====================

class Entidad(ABC):
    """Clase abstracta que representa una entidad general del sistema"""
    
    def __init__(self, id_entidad: str, nombre: str):
        self._id = id_entidad
        self._nombre = nombre
        self._fecha_creacion = datetime.now()
    
    @abstractmethod
    def mostrar_informacion(self) -> str:
        """Método abstracto para mostrar información de la entidad"""
        pass
    
    @abstractmethod
    def validar(self) -> bool:
        """Método abstracto para validar la entidad"""
        pass
    
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if valor and len(valor.strip()) > 0:
            self._nombre = valor
        else:
            raise ValidacionError("El nombre no puede estar vacío")
    
    @property
    def fecha_creacion(self):
        return self._fecha_creacion
