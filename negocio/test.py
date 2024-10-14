import unittest
from ValidacionDatos import ValidadorCUIT

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
    
if __name__ == '__main__':
    unittest.main()
