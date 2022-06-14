class Polynom:
    
    def __init__(self, coef):
        self.coef = coef
    
    def evaluate(self, n, prime):
        """
        Método que evalua polinomio de grado n
        Args:
            n : Grado del polinomio
            prime : Número primo para calcular el módulo
        Returns:
            ans : Número resultante evaluado
        """
        ans = 0
        for c in reversed(self.coef):
            ans = ((ans * n) + c) % prime
        return ans
    
    def mulPoints(pts, n, k, xi, yi, prime):
        """
        Método que

        Args:
            pts : _description_
            n : _description_
            k : _description_
            xi : _description_
            yi : _description_
            prime : _description_

        Returns:
            ans : _description_
        """
        poly = []
        for i in range(len(pts)):
            if (i == k):
                continue
            num = (n - pts[i][0]) % prime
            den = (xi - pts[i][0]) % prime
            invD = pow(den, prime-2, prime)
            poly.append(num * invD)
        ans = 1
        for k in range(len(poly)):
            ans *= poly[k]
        return ans * yi
    
    def lagrange(pts, n, prime):
        """
        Método que 

        Args:
            pts : Lista de tuplas para los puntos en el plano 
            n : N
            prime : Número primo para calcular el módulo

        Returns:
            ans : _description_
        """
        ans = 0
        for i in range(len(pts)):
            xi, yi = pts[i]
            ans = (Polynom.mulPoints(pts, n, i, xi, yi, prime) + ans + prime) % prime
        return ans