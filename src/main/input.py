from getpass import getpass
import sys
import os
import getpass


class Input:
    
    def readC(self):
        """
        Método para leer los argumentos desde la términal y guardarlos
        en variables de la siguiente orden:
        
        """
        #Archivo donde se guardará las n evaluaciones 
        save_file = sys.argv[2]
        #Equivalente a n
        num_eval = int(sys.argv[3])
        #Equivalente a t
        min_pts = int(sys.argv[4])
        #Documento claro
        clr_doc = sys.argv[5]
        password = getpass.getpass("Escriba la contraseña: ")
        
        
        
        
        return (save_file, num_eval, min_pts, clr_doc, password)
    
    def readD(self):
        #Archivo con al menos t de n evaluaciones
        frg = sys.argv[2]
        #Archivo cifrado
        aes = sys.argv[3]
        return (frg, aes)
    
    def checkExceptionsC(self, save_file, num_eval, min_pts, clr_doc, password):
        if(not save_file.endswith()):
            raise TypeError("")
        if(not isinstance(num_eval, int)):
            raise TypeError("")
        if(not isinstance(min_pts, int)):
            raise TypeError("")
        
    def checkExceptionsD(self, t_eval_file, n_pair_file):
        if(not os.path.exists(t_eval_file)):
            raise TypeError("")
        if(not os.path.exists(n_pair_file)):
            raise TypeError("")