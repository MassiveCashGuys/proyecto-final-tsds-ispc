import re


def cuit_es_valido(cuit):
    return len(cuit) == 11 and cuit.isdigit()
    

def validar_formato_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|info|co|ar|mx|es|it|fr|uk|io)$'
    return re.match(patron, email) is not None


def pw_es_valido(password):
    return 8 <= len(password) <= 16 and re.search(r'[a-zA-Z0-9!@#$%^&*(),.?":{}|<>]', password) is not None


def validacion_existencia_datos(object_dao,valor_a_validar):
    return object_dao.get(valor_a_validar)

def tipo_de_dato(funcion_de_tipo,variable_de_tipo):

        while True:
            if variable_de_tipo:
                break
            else: 
                variable_de_tipo = funcion_de_tipo()

def extraccion_num_documento(cuit):
     num_documento = cuit[2:(len(cuit) - 1)]
     return ("0" * (8-len(num_documento)) + num_documento)