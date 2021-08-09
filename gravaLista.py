# Copyright (C) 2021  FRANCINALDO CARVALHO <francinaldo@protonmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isdir, isfile, join

#grava lista de arquivos com nome de processo no diretório indicado


def extraiNomesArquivos(myPath): #retorna lista com o nome dos arquivos no diretório informado
    onlyFiles = [f for f in listdir(myPath) if isfile(join(myPath, f))]
    return onlyFiles

def extraiNomesDiretorios(myPath): #retorna lista com o nome das pastas do diretório informado
    onlyDirs = [f for f in listdir(myPath) if isdir(join(myPath, f))]
    return onlyDirs

def gravaListaProcessos(myPath, option):
    if option == 1:
        listaDeProcessos = extraiNomesArquivos(myPath) #para extrair nome dos arquivos
    if option == 2:
        listaDeProcessos = extraiNomesDiretorios(myPath)#para extrair nome das pastas
    
    arquivo = open(myPath+"\lista.txt","a")
    for f in listaDeProcessos:
        #if "4" in f: #se tiver o número 4 no arquivo, é porque é um número de processo
        arquivo.write(f+"\n")
    arquivo.close()
            
def main():
    myPath = input("indique o caminho dos arquivos: ")
    gravaListaProcessos(myPath)
    print('feito.')
def main():
    op = 0
    while (op != 5):

        print("1 - grava lista com o nome dos arquivos em lista_a.txt")
        print("2 - grava lista com o nome dos diretórios em lista_d.txt")
        #print("3 - ...")
        #print("4 - ...")
        #print("5 - ...")
        #print("6 - ...")
        print("7 - Sair")
        
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            myPath = input("indique o path: ")
            gravaListaProcessos(myPath, 1)
            print('feito.')
        elif op == 2:
            myPath = input("diretório raiz: ")
            gravaListaProcessos(myPath, 2)
        #elif op == 3:
        #    caminho = input("Número do processo: ")
        #    verValidade(numProc)         
        #elif op == 4:
        #    caminho = input("diretório: ")
        #    extraiNomesArquivos(myPath)
        #elif op == 5:
        #    caminho = input("diretório: ")
        #    extraiNomesDiretorios(myPath)
        #elif op == 6:
        #    caminho = input("diretório: ")
        #    verificaNomes(myPath)
        elif op == 7:
            break
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == '__main__':
    main()




'''
arquivo = open("contatos.txt","a")
arquivo.write("Olá, mundo!") --> escreve no arquivo
arquivo.writelines(lista[])
arquivo.close()

'r' - leitura
'w' - sobrescreve
'x' - escreve(retorna erro caso já exista)
'a' - escreve no final do arquivo
'b' - modo binário
't' - modo de texto (padrão)
'+' - atualizar. tanto leitura como escrita

para leitura do arquivo:

arquivo = open("contatos.txt","r")
print(arquivo.readline(3)) -->  retorna os tres primeiros caracteres da primeira
                                linha do arquivo

print(arquivo.readlines()) -->  retorna todas as linhas do arquivo
arquivo.close()

'''
