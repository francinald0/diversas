#############################################################
#							    #
# Programa de formatação dos arquivos do legado para o pje  #
# Data: 05/02/2021					    #
# Autor: Francinaldo Carvalho de Oliveira Júnior	    #
# Versão: 0.1						    #
#							    #
#############################################################

# -*- coding: utf-8 -*-


import verificar
#rotinas para verificar se o número de processo é válido

import dividir
#divide arquivos em pdf em outros de menores, de modo a atender um limite

import grava_lista
#gera lista com os processo da pasta indicada

import otimizar
#reduz número do arquivo

import renomear
#renomeia arquivos para o padrão do CNJ


def main():
    op = 0
    while (op != 7):
        print("1 - Verificar número")
        print("2 - reduzir tamanho")
        print("3 - Dividir arquivos")
        print("4 - Renomear arquivos")
        print("5 - Criar arquivo com número dos processos(lista.txt)")
        print("6 - lançar fase 222-12 nos processos da lista")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            print("essa rotina verifica se os nomes atribuídos a um grupo de _
                  "subdiretórios em um mesmo diretório são válidos")
            caminho = input("indique o caminho dos arquivos: ")
            verificar.verificaProcessos(caminho)
        elif op == 2:
            otimizaArquivos()
        elif op == 3:
            caminho = input("indique o caminho do arquivo: ")
            dividir.dividirAoMeio(caminho)
        elif op == 4:
            renomeiaArquivos()
        elif op == 5:
            caminho = input("indique o caminho dos diretórios:")
            grava_lista.gravaListaProcessos(caminho)
        elif op == 6:
            caminho = input("indique o caminho do arquivo lista.txt")
            lancarFase.Mov22212(caminho)
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
