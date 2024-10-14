import re

class ValidadorCUIT:
    def __init__(self, cuit):
        self.cuit = cuit

    def es_valido(self):
        return len(self.cuit) == 11 and self.cuit.isdigit()
    
if __name__ == '__main__':
    cuit_validador = ValidadorCUIT("20123456789")
    if cuit_validador.es_valido():
        print("El CUIT es válido.")
    else:
        print("El CUIT no es válido.")