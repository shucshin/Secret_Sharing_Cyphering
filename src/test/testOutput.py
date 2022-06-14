import unittest
from main.output import *

class TestOutput(unittest.TestCase):
    """Prueba unittest para Salidas"""
    
    def writeC(self):
        """
        Test para verificar que los archivos cifrados sean de extensión 'aes' o 'frg'
        """
        aes = 'text.txt.aes'
        frg = 'text.txt.frg'
        self.assertTrue(aes.endswith('aes'))
        self.assertTrue(frg.endswith('frg'))
        
        
    def writeD(self):
        """
        Test para verificar que el archivo original no sea de 'aes' o 'frg'
        """
        filename = 'shamir.png'
        self.assertTrue(not filename.endswith('frg'))
        self.assertTrue(not filename.endswith('aes'))
        
    
  