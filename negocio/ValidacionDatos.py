import re

class ValidadorCUIT:
    def __init__(self, cuit):
        self.cuit = cuit

    def cuit_es_valido(self):
        return len(self.cuit) == 11 and self.cuit.isdigit()
    

class ValidadorEmail:
    def __init__(self, email):
        self.email = email

    def mail_es_valido(self):
        return self._validar_formato_email(self.email)

    def _validar_formato_email(self, email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|info|co|ar|mx|es|it|fr|uk|io)$'
        return re.match(patron, email) is not None


if __name__ == '__main__':

    ejemplos = [
        "alann@prueba.com",
        "ejemplo@dominio.org",
        "usuario@empresa.net",
        "nombre@escuela.edu",
        "contacto@gobierno.gov",
        "u.@gmail.com",
        "u.com.ar",
        "@com.ar",
        "chancla@",
    ]

    for email in ejemplos:
        email_validador = ValidadorEmail(email)
        if email_validador.mail_es_valido():
            print(f"El correo electrónico '{email}' es válido.")
        else:
            print(f"El correo electrónico '{email}' no es válido.")


    cuit_validador = ValidadorCUIT("20315756597")
    if cuit_validador.cuit_es_valido():
        print("El CUIT es válido.")
    else:
        print("El CUIT no es válido.")


