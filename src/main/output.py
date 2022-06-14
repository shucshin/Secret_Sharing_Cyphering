class Output:
    
    def makeAES(self, filename, encrypted):
        #Get the filename without the extension and add '.aes'
        out = open(filename + '.aes', 'wb')
        out.write(encrypted)
    
    def makeFRG(self, filename, evals):
        #Get the filename without the extension and add '.aes'
        out = open(filename + '.frg', 'w')
        out.write(evals)
        
    def getOriginal(self, filename, decrypted):
        #Escribe el contenido decifrado
        out = open(filename, 'wb')
        out.write(decrypted)