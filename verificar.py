#Verifica a validade do número do processo
#05/02/2021

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

def main():
    op = 0
    while (op != 5):
        print("1 - Verificar validade de um número")
        print("2 - Verificar validade dos nomes de diretórios")
        print("3 - Informar nome dos arquivos de um diretório")
        print("4 - Informar nome dos subdiretórios de um diretório")
        print("5 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            processo = input("informe o número do processo: ")
            if verValidade(processo):
                print("válido")
            else:
                print("inválido")

        elif op == 2:
            caminho = input("indique o caminho do diretório que possui subdiretórios: ")
            verificaProcessos(caminho)
            
        elif op == 3:
            caminho = input("indique o caminho do diretório: ")
            extraiNomesArquivos(caminho)
            
        elif op == 4:
            caminho = input("indique o caminho do diretório: ")
            extraiNomesDiretorios(caminho)
        elif op == 5:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
