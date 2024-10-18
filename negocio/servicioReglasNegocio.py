import bcrypt
from controllers.controllerPortafolio import cargar_saldo_inicial


def crear_encriptacion_password(password):
    salt = bcrypt.gensalt()
    print(salt)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed)
    return hashed


def validar_password(password_has, pas):
    return bcrypt.checkpw(pas.encode(), password_has)


def asignar_saldo_inicial(idporfolio):
    cargar_saldo_inicial(id_portafolio=idporfolio)
    return "Se han asignado $1.000.000 de saldo inicial"
