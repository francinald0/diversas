#############################################################
#															#
# Programa de formatação dos arquivos do legado para o pje	#
# Data: 04/11/2020											#
# Autor: Francinaldo Carvalho de Oliveira Júnior			#
# Versão: 0.0												#
#															#
#############################################################

# -*- coding: utf-8 -*-

import verificar

#def verificaProcessos():
#Verifica, no diretório raiz, se os números de processos atribuídos aos
#nomes das pastas que contém os arquivos dos volumes
#dos processos do legado são válidos.

#    print("opção 1\n")
    
def otimizaArquivos():
#Tenta reduzir o tamanho dos arquivos que superam 10MB localizados
#nas pastas e subpastas do diretório raiz
    print("opção 2\n")

def divideArquivos():
#Divide os arquivos maiores que 10MB em arquivos menores até que todos
#tenham o tamanho menor do que esse limite, renomeando os arquivos
#divididos, de modo que continuem na mesma sequencia.
    print("opção 3\n")

def renomeiaArquivos():
#Renomeia todos os arquivos para o formato exigido pelo CNJ, ou seja
# XXXXXXX-XX.XXXX.X.XX.XXXX_VXXX_XXX, com base no número do processo
#colhido a partir do nome da pasta localizada no diretório raiz.
    print("opção 4\n")

def main():
    op = 0
    while (op != 5):
        print("1 - Verificar números de processos")
        print("2 - Otimizar arquivos")
        print("3 - Dividir arquivos")
        print("4 - Renomear arquivos")
        print("5 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("indique o caminho dos arquivos: ")
            verificar.verificaProcessos(caminho)
        elif op == 2:
            otimizaArquivos()
        elif op == 3:
            divideArquivos()
        elif op == 4:
            renomeiaArquivos()
        elif op == 5:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
