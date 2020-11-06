#Verifica a validade do número do processo
#04/11/2020

from os import listdir
from os.path import isdir, isfile, join



def verValidade(numProc):
    #adequa a string do argumento número do processo(numProc)
    #ao padrão de 20 caracteres, acrescentando zeros ao início dela
    if (len(numProc)<20):
        qZeros = (20 - len(numProc))*"0"
        numProc = qZeros + numProc
    
    #isola dígito
    d1 = numProc[7]
    d2 = numProc[8]
    digito = d1+d2
    iDigito = int(digito) #transforma o dígito para o tipo inteiro

    #formata número para cálculo do módulo, ou seja
    #retira o dígito e inclui dois zeros ao final do número
    numProc = numProc[:7]+numProc[9:]+"00"
    np = int(numProc) #transforma o número do processo para o tipo inteiro

    #verifica se a condição é atendida, ou seja
    # se 98 menos o módulo entre o np e 97 é igual ao dígito.
    # se for igual, o número do processo é válido.
    modulo = np % 97
    if (98-modulo == iDigito):
        return True
    else:
        return False

#Teste

def extraiNomesArquivos(myPath):
    #mypath = "C:/python/estudos/teste"
    onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return onlyFiles

def extraiNomesDiretorios(myPath):
    #mypath = "C:/python/estudos/teste"
    onlyDirs = [f for f in listdir(myPath) if isdir(join(myPath, f))]
    return onlyDirs


def verificaProcessos(myPath):
    listaDeProcessos = extraiNomesDiretorios(myPath)
    for processo in listaDeProcessos:
        if verValidade(processo):
            print(processo + " é válido")
        else:
            print(processo + " é inválido")





#f = []
#for (dirpath, dirname, filenames) in walk(mypath):
#    f.extend(filenames)
#    break





#print(extraiNome("C:\python\estudos\teste"))

#if verValidade("254"):
#    print("válido")
#else:
#    print("inválido")





'''

#recebe número do processo
stringNumProcesso = input("informe o número do processo: ")

#isola dígito
d1 = stringNumProcesso[7]
d2 = stringNumProcesso[8]
digito = d1+d2
iDitigo = int(digito)

#formata número para cálculo do módulo, ou seja
#retira o dígito e inclui dois zeros ao final do número
stringNumProcesso = stringNumProcesso[:7]+stringNumProcesso[9:]+"00"
np = int(stringNumProcesso)

#verifica se a condição é atendida, ou seja
# se 98 menos o módulo entre o np e 97 é igual ao dígito.
# se for igual, o número do processo é válido.

modulo = np % 97
if (98-modulo == iDigito):
    print("válido")
else
    print("inválido')

'''


