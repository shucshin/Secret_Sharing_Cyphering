# Secret Sharing Cyphering

## Descripción:
Programa que usa el esquema de secreto compartido de Shamir para cifrar un dato ocultandolo en `n` diferentes datos con al menos `t ≤ n` cualquiera de ellos siendo posible descifrar el dato ocultado y recuperar el dato original.

## Ejecución:
Primero, clone el repositorio.

``` sh
git clone https://github.com/shucshin/Secret_Sharing_Cyphering.git
```

### Prerrequisitos:
Es necesario usar `python3` al momento de ejecutar.

Instalar los siguientes paquetes con los siguientes comandos
```sh
pip3 install pycrypto
pip3 install pycryptodome
```


### Pruebas: 
Para ejecutar las pruebas debe situarse en el directorio `src/` de la siguiente forma: 

```sh
cd Secret_Sharing_Cyphering/src/
```

Luego, ejecute: 

``` sh
python3 -m unittest discover 
```

### Programa:
Para ejecutar el proyecto debe situarse en el directorio `src/` de la siguiente forma: 

```sh
cd Secret_Sharing_Cyphering/src/
```

### Cifrar:
Formato
```sh
python3 main/main.py -c savefile n t cleardoc
```
Ejemplo 1
``` sh
python3 main/main.py -c shamir.png 10 3 sham/Vaporwave.png
```
Ejemplo 2
``` sh
python3 main/main.py -c shamir.txt 20 2 sham/Hard.txt
```
### Descifrar:
Formato
```sh
python3 main/main.py -d filename.frg filename.aes
```
Ejemplo 1
``` sh
python3 main/main.py -d shamir.png.frg shamir.png.aes
```
Ejemplo 2
``` sh
python3 main/main.py -d shamir.txt.frg shamir.txt.aes
```

### Verificar:
Después de haber ejecutado estos comandos, puede abrir el archivo para verificar el resultado con:

Ejemplo 1
```sh
open shamir.png
```
Ejemplo 2
```sh
open shamir.txt
```

## Integrante: 
- Ui Chul Shin

## Bibliografía: 

1. [IMPLEMENTACIÓN DEL ESQUEMA DE INTERCAMBIO SECRETO DE SHAMIR EN PYTHON](https://es.acervolima.com/implementacion-del-esquema-de-intercambio-secreto-de-shamir-en-python/)
1. [Secret Sharing Schemes](https://pycryptodome.readthedocs.io/en/latest/src/protocol/ss.html)
1. [AES-256 Cipher – Python Cryptography Examples](https://blog.boot.dev/cryptography/aes-256-cipher-python-cryptography-examples/)
1. [tkinter — Interface de Python para Tcl/Tk](https://cryptomarketpool.com/convert-a-string-to-sha256-in-python/)
1. [Convert a string to SHA256 in Python](https://discord.com/channels/800826113906835474/800826113906835476/951709366275407922)
1. [Criptografía en Python - AES](https://pythondiario.com/2020/07/criptografia-en-python-aes.html)
1. [Implementing Shamir’s Secret Sharing Scheme in Python](https://www.geeksforgeeks.org/implementing-shamirs-secret-sharing-scheme-in-python/)
