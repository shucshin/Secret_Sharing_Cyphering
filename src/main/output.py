class Output:
    """Clase para manejo de salida"""
    
    def makeAES(self, filename, encrypted):
        """
        Método que genera el archivo cifrado con la extensión .aes
        
        Parámetros: 
            filename : nombre del archivo con la que vamos a generar el archivo .aes
            encrypted : documento cifrado
        """
        out = open(filename + '.aes', 'wb')
        out.write(encrypted)
    
    def makeFRG(self, filename, evals):
        """
        Método que genera el archivo con las n evaluaciones
        con la extensión .frg
        
        Parámetros:
            filename : nombre del archivo con la que vamos a generar el archivo .frg
            evals : las n parejas evaluaciones del polinomio
        """
        out = open(filename + '.frg', 'w')
        out.write(evals)
        
    def getOriginal(self, filename, decrypted):
        """
        Método que genera el archivo original
        
        Parámetros:
            filename : nombre del archivo con la que vamos a generar el archivo descifrado
            decrypted : documento claro
        """
        out = open(filename, 'wb')
        out.write(decrypted)