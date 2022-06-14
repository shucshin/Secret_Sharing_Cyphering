import unittest
from main.polynom import *

class TestPolynom(unittest.TestCase):
    """Prueba unittest para Polinomios"""
    
    def testLagrange(self):
        """
        Test para verificar que la fórmula de interpolación de 
        lagrange esté bien implementada comparando con los 
        resultados sacados manualmente. (x^2+2x+1, -x^2-x+5)
        """
        pts = [
            [(0,1), (1,4), (2,9), (4,25), (6,49)],
            [(0,5), (1,3), (2,-1), (3,-7)]
        ]
        ans = [4, 3]
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        for i in range(len(ans)):
            num = Polynom.lagrange(pts[i], 1, bigPrime)
            self.assertTrue(num == ans[i])
    
    def testEvaluate(self):
        """
        Test para verificar que el método que evalua el
        polinomio con operaciones aritméticas esté biem
        implementada comparando con los resultados sacados
        manualmente.
        """
        poly = [
            [1,2,3,4,5],
            [5,4,3,2,1],
            [1,3,5,7,9],
            [2,4,6,8,0]
        ]
        polyL = list(map(lambda a: Polynom(a), poly))
        nums = [15, 15, 25, 20]
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        for i in range(len(nums)):
            polyi = polyL[i].evaluate(1, bigPrime)
            self.assertTrue(polyi == nums[i])
            
        
    
  