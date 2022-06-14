class Polynom:
    """Clase para manejo de polinomios"""
    
    def __init__(self, coef):
        """
        Constructor de la clase para pasar el coeficiente
        como argumento automáticamente.
        """
        self.coef = coef
    
    def evaluate(self, n, prime):
        """
        Método que evalua polinomio de grado m con operaciones
        aritméticas.
        
        Parámetros:
            n : Número con la que se evaluará el polinomio
            prime : Número primo para calcular el módulo
        Regresa:
            ans : Número resultante evaluado
        """
        ans = 0
        for c in reversed(self.coef):
            ans = ((ans * n) + c) % prime
        return ans
    
    def mulPoints(pts, n, k, xi, yi, prime):
        """
        Método que calcula la interpolación polynomial en x de índice k

        Parámetros:
            pts : Lista de tuplas para los puntos en el plano 
            n : Número con la que se evaluará el polinomio
            k : índice
            xi : Punto donde se hará la interpolación el polinomio
            yi : P(xi)
            prime : Número primo para calcular el módulo

        Returns:
            ans : Número resultante evaluado
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
        Método que aplica la fórmula de interpolación de lagrange

        Parámetros:
            pts : Lista de tuplas para los puntos en el plano 
            n : Número con la que se evaluará el polinomio
            prime : Número primo para calcular el módulo

        Returns:
            ans : Número resultante evaluado
        """
        ans = 0
        for i in range(len(pts)):
            xi, yi = pts[i]
            mp = Polynom.mulPoints(pts, n, i, xi, yi, prime)
            ans = (mp + ans + prime) % prime
        return ans