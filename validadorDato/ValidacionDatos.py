import re
from backend.clasesDAO import usuario_dao
from backend.clasesDAO import inversor_dao
from controllers import controllerUsuario
from negocio import servicioReglasNegocio

def pw_es_valido(password):
    return 8 <= len(password) <= 16 and re.search(r'[a-zA-Z0-9!@#$%^&*(),.?":{}|<>]', password) is not None


def tipo_de_dato(funcion_de_tipo,variable_de_tipo):

        while True:
            if variable_de_tipo:
                return variable_de_tipo
            else: 
                variable_de_tipo = funcion_de_tipo()
                return 

def extraccion_num_documento(cuit):
     num_documento = cuit[2:(len(cuit) - 1)]
     return ("0" * (8-len(num_documento)) + num_documento)


def validar_formato_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|info|co|ar|mx|es|it|fr|uk|io)$'
    return re.match(patron, email) is not None


def valida_existencia_mail_bd(email):
    user_dao = usuario_dao.Usuario_Dao()
    user = user_dao.get(email)
    
    if user is None and validar_formato_email(email):
        return True
    else:
        return False


def cuit_es_valido(cuit):
    return len(cuit) == 11 and cuit.isdigit()
    

def valida_existencia_cuit_en_db(cuit):
    cuit_dao = inversor_dao.InversorDao()
    cuit_existente = cuit_dao.get(cuit)

    if cuit_existente is None and cuit_es_valido(cuit):
        return True
    else:
        return False


