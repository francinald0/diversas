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

def verValidade(numProc):
    #adequa a string do argumento número do processo(numProc)
    #ao padrão de 20 caracteres, acrescentando zeros ao início dela
    #if (len(numProc)<20):
    #    qZeros = (20 - len(numProc))*"0"
    #    numProc = qZeros + numProc
    
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

def removeMaskLine(proc):

    #blacklist = set('.-\"')
    #proc.join(c for c in proc if c not in blacklist)
    string = proc
    string = string.replace('.', '')
    string = string.replace('-', '')
        
    return string

def addZerosLeft(proc):

    if (len(proc) < 20):
        qZerosLeft = (20 - len(proc))*"0"
        proc = qZerosLeft + proc

    return proc

def normalizeProcess(lst): #remove mask and fill with zeros ahead
    listaOut = []
    #listaOut.clear()
    for l in lst:
        proc_ = removeMaskLine(l)
        proc_ = addZerosLeft(proc_)
        listaOut.append(proc_)

    return listaOut

def verificaProcessos(lista):
    listaDeProcessos = normalizeProcess(lista)
    
    for processo in listaDeProcessos:
        if verValidade(processo):
            print("o processo "+processo+" é válido")
        else:
            print("o processo "+processo+" não é válido")

def buscaProcessos(fileName):
    processos = []
    with open(fileName, 'r') as a_file:
        list_of_lines = a_file.read().splitlines()
        a_file.close()

    for i in list_of_lines:
        #if comonTermInProc in i:
        processos.append(i)
    return processos

    
def main():    

    
    op = 0
    while (op != 7):
        print("1 - verificar se o número do processo é válido")
        print("2 - ...")
        print("3 - ...")
        print("4 - ...")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("indique o nome do arquivo(caminho completo): ")
            procList = buscaProcessos(caminho)
            verificaProcessos(procList)
        #elif op == 2:
        #    pass

        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
