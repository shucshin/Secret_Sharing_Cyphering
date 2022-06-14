import unittest
import re
from main.shamir import *

class TestShamir(unittest.TestCase):
    """Prueba unittest para la clase Shamir"""
    
    def testKey(self):
        """
        Test para verificar que la contraseña convertida a
        SHA-256 sea correctamente de 256 bits (32 caracteres)
        """
        sha = Shamir()
        password = 'holimundo'
        key = sha.getKey(password)
        self.assertTrue(len(bytes(key)) == 32)
        