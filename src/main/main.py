import sys
sys.path.insert(1, '../../Proyecto3_MyP_2022_2/src')
from input import *
from shamir import *
from output import *

class Main:
    
    """Instanciando clases"""
    inp = Input()
    sha = Shamir()
    out = Output()
    
    #Bandera -c para Cifrar
    if sys.argv[1] == '-c':
        """Lectura de los argumentos, guarda la contraseña en
        password y se usa como parámetro para obtener la llave
        que se usará para obtener el archivo cifrado junto con
        el archivo claro como 'aes' y las n evaluaciones del 
        polinomio junto con n y t como 'evals'"""
        args = inp.readC()
        password = args[4]
        key = sha.getKey(password)
        clear = open(args[3], "rb").read()
        aes = sha.getAesC(clear, key)
        evals = sha.getEvaluations(args[1], args[2], key)
        
        """Genera los archivos .aes y .frg respectivamente"""
        out.makeAES(args[0], aes)
        out.makeFRG(args[0], evals)
        
    #Bandera -d para Descifrar
    elif sys.argv[1] == '-d':
        """Lectura de los argumentos, lee el archivo .frg como evals
        y .aes como ciphered para usarlos como parámetros en 
        la función para descifrar y guardarlo en decrypted"""
        args = inp.readD()
        evals = open(args[0], "r").read()
        ciphered = open(args[1], "rb").read()
        decrypted = sha.decrypt(evals, ciphered)
        
        """Se obtiene el nombre el archivo original y
        escribe el dato descifrado en ese nombre"""
        filename = args[0].replace('.frg', '')
        out.getOriginal(filename, decrypted)
        
    else:
        print(TypeError("Error: La bandera debe ser -c o -d"))
    
    