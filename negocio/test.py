import unittest
from ValidacionDatos import ValidadorCUIT, ValidadorEmail


class TestValidarCuit(unittest.TestCase):

    def test_cuit_correcto(self):
        self.assertTrue(ValidadorCUIT("20123456789").es_valido())
        self.assertTrue(ValidadorCUIT("27876543210").es_valido())
    
    def test_cuit_incorrecto_long(self):
        self.assertFalse(ValidadorCUIT("2012345678").es_valido())
        self.assertFalse(ValidadorCUIT("201234567891").es_valido())

    def test_cuit_inc_caracteres(self):
        self.assertFalse(ValidadorCUIT("20A12345678").es_valido())
        self.assertFalse(ValidadorCUIT("20#23456789").es_valido())
    
class TestValidarEmail(unittest.TestCase):
    def test_email_correcto(self):
        self.assertTrue(ValidadorEmail("ejemplo@dominio.com").es_valido())
        self.assertTrue(ValidadorEmail("nombre.apellido@sub.dominio.com").es_valido())
        self.assertTrue(ValidadorEmail("usuario+etiqueta@dominio.com").es_valido())
    
    def test_email_incorrecto_sin_arroba(self):
        self.assertFalse(ValidadorEmail("ejemplodominio.com").es_valido())
        self.assertFalse(ValidadorEmail("ejemplo.dominio.com").es_valido())

    def test_email_incorrecto_sin_dominio(self):
        self.assertFalse(ValidadorEmail("ejemplo@").es_valido())
        self.assertFalse(ValidadorEmail("ejemplo@dominio").es_valido())

    def test_email_incorrecto_caracteres_invalidos(self):
        self.assertFalse(ValidadorEmail("ejemplo@dominio!.com").es_valido())
        self.assertFalse(ValidadorEmail("ejemplo@dominio#.com").es_valido())

if __name__ == '__main__':
    unittest.main()
    