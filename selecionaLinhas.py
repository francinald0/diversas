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

import codecs
#import pyautogui
#import pyperclip
#import os
#from os import listdir
#from os.path import isdir, isfile, join


inText = "D:\\scripts\\python\\rotinas.txt"
outText = "D:\\scripts\\python\\rotinas.o.txt"


def formatProc(processo):
    proc = removeMaskLine(processo)
    proc = addZerosLeft(proc)

    return proc



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


def searchStringPrintFile(searchTerm, inputFile = inText, outputFile = outText):
# search for a string on inputFile and print the lines wich contain searchTerm
# in outputFile
    comonTermInProc = searchTerm
    occurrences = []
    with codecs.open(inputFile, 'r',encoding='utf-8',errors='ignore') as i_file:
        list_of_lines = i_file.read().splitlines()
        i_file.close()
    for l in list_of_lines:
        if searchTerm in l:
            occurrences.append(l)
            
    with open(outputFile, 'w') as o_file:
    #a_file.writelines(lista)
        for l in occurrences:
            o_file.write(l+"\n")
        o_file.flush()#don't know why...Its about garbage colector
        o_file.close()
    
    return occurrences

def searchStringPrintScreen(searchTerm, inputFile = inText):
# search for a string on inputFile and print the lines wich contain searchTerm
# in screen
    comonTermInProc = searchTerm
    occurrences = []
    with codecs.open(inputFile, 'r',encoding='utf-8',errors='ignore') as i_file: #encoding='utf-8' necessary
        list_of_lines = i_file.read().splitlines()
        i_file.close()
    for l in list_of_lines:
        if searchTerm in l:
            occurrences.append(l)
    for oc in occurrences:
        print(oc)        
     

def main():
      
    #print("")
    termo = input("digite o termo a ser pesquisado: ")
    print("insira a opção: ")
    op = 0
    while (op != 7):
        print("1 - imprimir resultado em arquivo")
        print("2 - imprimir resultado na tela")
        print("3 - inserir novo termo")
#        print("4 - ...")
#        print("5 - ...")

        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            searchStringPrintFile(termo)
        elif op == 2:          
            searchStringPrintScreen(termo)
        elif op == 3:          
            termo = input("digite o termo a ser pesquisado: ")
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()

