from getpass import getpass
import sys
import os
import getpass

class Input:
    """Clase para manejo de entrada"""
    
    def readC(self):
        """
        Método para leer los argumentos desde la términal, 
        obtener la contraseña indicada por el usuario,
        detectar posibles excepciones y extraer una
        lista de ellos.
        """
        save_file = sys.argv[2]
        num_eval = int(sys.argv[3])
        min_pts = int(sys.argv[4])
        clr_doc = sys.argv[5]
        self.checkExceptionsC(save_file, num_eval, min_pts, clr_doc)
        password = getpass.getpass("Escriba la contraseña: ")
        return (save_file, num_eval, min_pts, clr_doc, password)
    
    def readD(self):
        """
        Método para leer los argumentos desde la términal,
        obtener el nombre del archivo con al menos t de n 
        evaluaciones como .frg y al archivo cifrado como .aes, 
        detectar posibles excepciones y extraer una lista de ellos.
        """
        frg = sys.argv[2]
        aes = sys.argv[3]
        self.checkExceptionsD(frg, aes)
        return (frg, aes)
    
    def checkExceptionsC(self, save_file, num_eval, min_pts, clr_doc):
        """
        Método para checar que los argumentos con la lectura de
        bandera -d sean correctos.
        """
        if(not os.path.splitext(save_file)[1].startswith('.')):
            raise TypeError("El archivo no tiene extensión")
        if(not os.path.splitext(clr_doc)[1].startswith('.')):
            raise TypeError("El archivo no tiene extensión")
        if(not isinstance(num_eval, int) or num_eval < 3):
            raise TypeError("El número de evaluaciones debe ser mayor que 2")
        if(not isinstance(min_pts, int) or min_pts > num_eval):
            raise TypeError("El número de puntos necesarios no puede ser mayor que el número de evaluaciones")
        
    def checkExceptionsD(self, frg, aes):
        """
        Método para checar que los argumentos con la lectura de
        bandera -d sean correctos.
        """
        if(not os.path.exists(frg) or not frg.endswith('frg')):
            raise TypeError("No está el archivo .frg")
        if(not os.path.exists(aes) or not aes.endswith('aes')):
            raise TypeError("No está el archivo .aes")