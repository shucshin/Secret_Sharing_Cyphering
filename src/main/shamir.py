import hashlib
import random
import sys
sys.path.insert(1, '../../Proyecto3_MyP_2022_2/src/main')
from Crypto.Cipher import AES
from Crypto.Protocol.SecretSharing import Shamir
from input import *
from polynom import *

class Shamir:
    """Clase para manejar cifrado y descifrado de datos"""
    
    #Funciones para cifrar
    def getKey(self, password):
        """
        Método que convierte una contraseña a una versión de 256 bits
        
        Parámetros:
            password : La contraseña escrita por el usuario
        Regresa:
            key : código hash con SHA-256 (32 caracteres)
        """
        key = hashlib.sha256(password.encode('utf8')).digest()
        return key
    
    def getAesC(self, file, password):
        """
        Método que encrypta el mensaje usando AES

        Parámetros:
            file : el archivo claro
            password : la llave de 256 bits (32 caracteres)
        Regresa:
            aesEnc : mensaje encriptado
        """
        aes = AES.new(password, AES.MODE_CFB, 16*b'\0')
        aesEnc = aes.encrypt(file)
        return aesEnc
        
    def generateBits(b, t):
        """
        Método que genera una serie de t enteros en el rango de 256 bits

        Parámetros:
            b : rango de bits, en este caso será 256
            t : Número de enteros que se generará
        Regresa:
            list(bits) : lista de bits generados arbitrariamente
        """
        bits = set()
        while len(bits) < t:
            bits.add(int(random.getrandbits(b)))
        return list(bits)
        
    def getEvaluations(self, n, t, key):
        """
        Método que genera un polinomio para poder evaluarla con n puntos

        Parámetros:
            n : número de evaluaciones totales (n > 2)
            t : número de puntos necesarios para descifrar (1 < t <= n)
            key : la llave de código hash con SHA-256
        Regresa:
            frg: las n evaluaciones del polinomio
        """
        dom = Shamir.generateBits(256, n)
        coef = Shamir.generateBits(256, t-1)
        coef.insert(0, int.from_bytes(key, byteorder='little'))
        poly = Polynom(coef)
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        evals = [(i, poly.evaluate(i, bigPrime)) for i in dom]
        frg = '\n'.join(['({},{})'.format(a[0], a[1]) for a in evals])
        return frg
    

    #Funciones para descifrar
    def getAesD(ciphered, byte):
        """
        Método que descifra el mensaje usando AES

        Parámetros:
            ciphered : contenido del archivo .aes
            byte : la contraseña convertido en bytes
        Regresa:
            aesDec : mensaje descifrado
        """
        aes = AES.new(byte, AES.MODE_CFB, 16*b'\0')
        aesDec = aes.decrypt(ciphered)
        return aesDec
    
    def divide(evals):
        """
        Método que divide los puntos en tuplas que contiene
        su evaluación correspondiente y se agregan
        a una lista de tuplas llamado pts.

        Parámetros:
            evals : contenido del archivo .frg

        Regresa:
            pts : lista de tuplas de las evaluaciones divididas
        """
        lines = evals.strip().split('\n')
        pts = []
        for l in lines:
            l = l[1:-1].split(',')
            pts.append((int(l[0]), int(l[1])))
        return pts

    def decrypt(self, evals, ciphered):
        """
        Método que recibe el contenido del archivo .frg y
        archivo .aes para poder obtener la contraseña y 
        decifrar el archivo

        Parámetros:
            evals : contenido del archivo .frg
            ciphered : contenido del archivo .aes

        Regresa:
            clear : documento claro
        """
        pts = Shamir.divide(evals)
        bigPrime = 5210644015679228794060694325390955853335898483908056458352183851018372555735221
        password = Polynom.lagrange(pts, 0, bigPrime)
        byte = password.to_bytes(32, byteorder='little')
        clear = Shamir.getAesD(ciphered, byte)
        return clear