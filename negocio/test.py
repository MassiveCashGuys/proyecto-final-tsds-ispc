import unittest
from ValidacionDatos import validar_cuit

class TestValidarCUIT(unittest.TestCase):
    def test_cuit_valido(self):
        self.assertTrue(validar_cuit("20357856591"))

    def test_cuit_mas_corto(self):
        self.assertFalse(validar_cuit("1234567891"))
    
    def test_cuit_mas_largo(self):
        self.assertFalse(validar_cuit("123456789123"))
    
    def test_letras(self):
        self.assertFalse(validar_cuit("123a456b789"))
    
    def test_caracteres(self):
        self.assertFalse(validar_cuit("20-358659.1"))

if __name__ == '__main__':
    unittest.main()