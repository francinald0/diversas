#Verifica a validade do número do processo
#05/02/2021

from os import listdir
from os.path import isdir, isfile, join

#---lista de funções---
#def removerPastasBkp(myPath):
#def verificaErros(myPath):
#def verValidade(numProc):
#def extraiNomesArquivos(myPath):
#def extraiNomesDiretorios(myPath):
#def verificaNomes(myPath):

def removerPastasBkp(myPath):
    listaPastasBkp = []
    for folderName, subfolders, filenames in os.walk(myPath):
        #print(folderName)
        #print(folderName[-3:])
        if folderName[-3:]=="bkp":
            listaPastasBkp.append(folderName)
    for pasta in listaPastasBkp:
        shutil.rmtree(pasta)

#verificar nomes de pastas que possuem letras
#verificar nomes de pastas de volumes com erro de digitação
#verificar arquivos com tamanho = 0
def verificaErros(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        for filename in filenames:
            pathArquivo = folderName+"\\"+filename
            tamanho = os.path.getsize(pathArquivo)
            if tamanho == 0:
                print(pathArquivo+": "+tamanho)

            #print(folderName+"\\"+filename)
            #print("nome: "+filename+"tamanho: "+os.stat(filename).st_size)
            #print(os.path.join(myPath,filename))
            #pathArquivo = os.path.abspath(filename)
            #tamanho = os.path.getsize(pathArquivo)
            #if tamanho > 10485760:
                #print(filename + " maior que 10MB")


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


def extraiNomesArquivos(myPath): #retorna lista com o nome dos arquivos no diretório informado
    onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return onlyFiles

def extraiNomesDiretorios(myPath): #retorna lista com o nome das pastas do diretório informado
    onlyDirs = [f for f in listdir(myPath) if isdir(join(myPath, f))]
    return onlyDirs

    
def verificaNomes(myPath):
    listaDeProcessos = extraiNomesDiretorios(myPath)
    for processo in listaDeProcessos:
        if verValidade(processo):
            print(processo + " é válido")
        else:
            print(processo + " é inválido")


def main():
    op = 0
    while (op != 5):

        print("1 - removerPastasBkp(myPath)")
        print("2 - verificaErros(myPath)")
        print("3 - verValidade(numProc)")
        print("4 - extraiNomesArquivos(myPath)")
        print("5 - extraiNomesDiretorios(myPath)")
        print("6 - verificaNomes(myPath)")
        print("7 - Sair")
        
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("diretório raiz: ")
            removerPastasBkp(myPath)
        elif op == 2:
            caminho = input("diretório raiz: ")
            verificaErros(myPath)
        elif op == 3:
            caminho = input("Número do processo: ")
            verValidade(numProc)         
        elif op == 4:
            caminho = input("diretório: ")
            extraiNomesArquivos(myPath)
        elif op == 5:
            caminho = input("diretório: ")
            extraiNomesDiretorios(myPath)
        elif op == 6:
            caminho = input("diretório: ")
            verificaNomes(myPath)
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
