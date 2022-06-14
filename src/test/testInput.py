import unittest
from main.input import *

class TestInput(unittest.TestCase):
    """Prueba unittest para Polinomios"""
    
    def testInputC(self):
        """
        Test para checar si el método encuentra argumentos malos 
        para la bandera -c
        """
        inp = Input()
        save_file = 'shamir.png'
        num_eval = 10
        min_pts = 3
        clr_doc = 'shamir/Vaporwave.png'
        fail = ['hello', 1, 999, 'hola']
        self.assertRaises(TypeError, inp.checkExceptionsC, fail[0], num_eval, min_pts, clr_doc)
        self.assertRaises(TypeError, inp.checkExceptionsC, save_file, fail[1], min_pts, clr_doc)
        self.assertRaises(TypeError, inp.checkExceptionsC, save_file, num_eval, fail[2], clr_doc)
        self.assertRaises(TypeError, inp.checkExceptionsC, save_file, num_eval, min_pts, fail[3])
        
    def testInputD(self):
        """
        Test para checar si el método encuentra argumentos malos 
        para la bandera -d
        """
        inp = Input()
        frg = 'shamir.png.frg'
        aes = 'shamir.png.aes'
        fail = ['sha', 'mir']
        self.assertRaises(TypeError, inp.checkExceptionsD, fail[0], aes)
        self.assertRaises(TypeError, inp.checkExceptionsD, frg, fail[1])
    