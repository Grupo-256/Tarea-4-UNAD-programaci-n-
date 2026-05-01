import re
class Cliente:
    def __init__(self, nombre, email, cedula):
        self.nombre = nombre
        self.email = email
        self.cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        patron = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if not re.match(patron, valor.lower()):
            raise ValueError("El formato del correo electrónico es inválido.")
        self._email = valor

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not str(valor).isdigit():
            raise ValueError("La cédula/ID debe contener solo números.")
        self._cedula = valor
