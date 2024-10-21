import bcrypt
from datetime import datetime
""" from controllers.controllerPortafolio import cargar_saldo_inicial """


def crear_encriptacion_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def validar_password(password, password_has):
    password_has = password_has.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), password_has)


""" def asignar_saldo_inicial(idporfolio):
    cargar_saldo_inicial(id_portafolio=idporfolio)
    return "Se han asignado $1.000.000 de saldo inicial" """

def definir_fecha_actual():
    fecha_actual = datetime.now()
    fecha_formato = fecha_actual.strftime('%Y-%m-%d')
    return fecha_formato
