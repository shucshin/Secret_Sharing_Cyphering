import hashlib
import random
from Crypto.Cipher import AES
from Crypto.Protocol.SecretSharing import Shamir
from input import *
from polynom import *

class Shamir:
    #Funciones para cifrar
    def getKey(self, password):
        #Regresa la versión de 256-byte de la contraseña escrita por el usuario
        key = hashlib.sha256(password.encode('utf8')).digest()
        return key
    
    def getAesC(self, file, password):
        #Regresa el mensaje encryptado usando AES
        aes = AES.new(password, AES.MODE_CFB, 16*b'\0')
        aesEnc = aes.encrypt(file)
        return aesEnc
        
    def generateBits(b, t):
        """
        Genera una serie de t enteros en el rango de 256 bits
        """
        bits = set()
        while len(bits) < t:
            bits.add(int(random.getrandbits(b)))
        return list(bits)
        
    def getEvaluations(self, n, t, key):
        """
        Genera un polinomio para poder evaluarla con n puntos
        """
        dom = Shamir.generateBits(256, n)
        coef = Shamir.generateBits(256, t-1)
        coef.insert(0, int.from_bytes(key, byteorder='little'))
        poly = Polynom(coef)
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        evals = [(i, poly.evaluate(i, bigPrime)) for i in dom]
        frg = '\n'.join(['({},{})'.format(a[0], a[1]) for a in evals])
        return frg
    

    #Funciones para decifrar
    def getAesD(txt, password):
        #Regresa el mensaje decryptado usando AES
        aes = AES.new(password, AES.MODE_CFB, 16*b'\0')
        aesDec = aes.decrypt(txt)
        return aesDec
    
    def divide(points):
        """
        Divide los puntos en tuplas que contiene
        su evaluación correspondiente y se agregan
        a una lista de tuplas llamado pts.
        """
        lines = points.strip().split('\n')
        pts = []
        for l in lines:
            l = l[1:-1].split(',')
            pts.append((int(l[0]), int(l[1])))
        return pts

    def decrypt(self, evals, ciphered):
        """
        Recibe el contenido del archivo .frg para poder
        obtener la contraseña y decifrar el archivo
        """
        pts = Shamir.divide(evals)
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        password = Polynom.lagrange(pts, 0, bigPrime)
        byte = password.to_bytes(32, byteorder='little')
        clear = Shamir.getAesD(ciphered, byte)
        return clear