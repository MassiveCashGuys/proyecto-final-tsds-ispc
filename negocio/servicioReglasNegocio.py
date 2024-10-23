import datetime
import msvcrt
import bcrypt
from controllers.controllerPortafolio import cargar_saldo_inicial


def crear_encriptacion_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def validar_password(password, password_has):
    password_has = password_has.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), password_has)

# Método para ocultar la contraseña con asteriscos
def input_con_asteriscos(prompt):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        tecla = msvcrt.getch()
        if tecla == b'\r':  # Enter (fin de la contraseña)
            break
        elif tecla == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += tecla.decode('utf-8')
            print('*', end='', flush=True)
    print()  # Salto de línea al final
    return password

""" def asignar_saldo_inicial(idporfolio):
    cargar_saldo_inicial(id_portafolio=idporfolio)
    return "Se han asignado $1.000.000 de saldo inicial" """

def definir_fecha_actual(formato):
    fecha_actual = datetime.datetime.now()
    fecha_formato = fecha_actual.strftime(formato)
    return fecha_formato

def formato_fecha():
    return '%Y-%m-%d'

def formato_fecha_hora():
    return '%Y-%m-%d-%H:%M:%S'
     