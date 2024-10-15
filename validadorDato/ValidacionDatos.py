import re


def cuit_es_valido(cuit):
    return len(cuit) == 11 and cuit.isdigit()
    

def validar_formato_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|info|co|ar|mx|es|it|fr|uk|io)$'
    return re.match(patron, email) is not None


def pw_es_valido(password):
    return 8 <= len(password) <= 16 and re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', password) is not None

