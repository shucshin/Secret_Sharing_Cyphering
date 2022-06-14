import sys
sys.path.insert(1, '../../Proyecto3_MyP_2022_2/src')
from input import *
from shamir import *
from output import *

class Main:
    
    inp = Input()
    sha = Shamir()
    out = Output()
    
    if sys.argv[1] == '-c':
        args = inp.readC()
        #Guardar la contraseña en el variable password
        password = args[4]
        #Obtener la llave usando password como argumento 
        key = sha.getKey(password)
        #Lectura del archivo claro
        clear = open(args[3], "rb").read()
        #Obtención del archivo cifrado
        aes = sha.getAesC(clear, key)
        
        
        #Evals tiene las n evaluaciones
        evals = sha.getEvaluations(args[1], args[2], key)
        
        
        #Genera el archivo .aes
        out.makeAES(args[0], aes)
        #Genera el archivo .frg
        out.makeFRG(args[0], evals)
        
        
    elif sys.argv[1] == '-d':
        args = inp.readD()
        evals = open(args[0], "r").read()
        ciphered = open(args[1], "rb").read()
        #evals = .frg, ciphered = .aes
        decrypted = sha.decrypt(evals, ciphered)
        filename = args[1].replace('.aes', '')
        out.getOriginal(filename, decrypted)
        
    else:
        TypeError("")
    
    