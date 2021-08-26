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


import pyautogui
import pyperclip
import os
from os import listdir
from os.path import isdir, isfile, join

fileProcessos = "D:\\scripts\\python\\lista_de_processos.txt"

def inserirNosCampos(processo):
    pyperclip.copy(processo)
    pyautogui.hotkey('ctrl','v')
    #pyperclip.paste
    pyautogui.press('tab')
    pyautogui.PAUSE = 0.5
    
    return 0

def insertOracleMalaDireta(listaMD):
    pyautogui.moveTo(164,180,0.2)
    pyautogui.click()
    for processo in listaMD:
        inserirNosCampos(processo)
    return 0

def insertOracleMovimentacao(listaMov):
    pyautogui.moveTo(164,180,0.2)
    pyautogui.click()
    for processo in listaMov:
        inserirNosCampos(processo)
    return 0

def insertOracleLocalizacao(listaLoc):
    pyautogui.moveTo(164,180,0.2)
    pyautogui.click()
    for processo in listaLoc:
        inserirNosCampos(processo)
    return 0

def formatProc(processo):
    proc = removeMaskLine(processo)
    proc = addZerosLeft(proc)

    return proc

def validProc(numProc): 
    d1 = numProc[7]
    d2 = numProc[8]
    
    digito = d1+d2
  
    iDigito = int(digito)

    numProc = numProc[:7] + numProc[9:] + "00"
      
    np = int(numProc)

    modulo = np % 97

    if (98-modulo == iDigito):
        return True
    else:
        return False

def verificaValidadeLista(listv):
    # retorna False se figurar na lista algum processo com
    # número inválido
    listaValida = True
    for processo in listv:
        numProc = formatProc(processo)
        if validProc(numProc):
            print(processo + " é válido")  
        else:
            print(processo + " NÃO é válido")
            listaValida = False

    if listaValida:
        return True
    else:
        return False

def removeMaskLine(proc):
    #remove pontos e hífens
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

def sanitizedList():
    with open(file, 'r') as a_file:
        list_of_lines = a_file.read().splitlines()
        #lines = f.read().splitlines()
        lstNormalized = normalizeProcess(list_of_lines)
        a_file.close()
    return lstNormalized

def sanitizeFile(lista):

    with open(file, 'w') as a_file:
        a_file.writelines(lista)
        a_file.close()

def main():
    
    lista = sanitizedList() # exclui a máscara e inclui zeros na frente do número
                            # de modo que a string tenha 20 caracteres
    
    if verificaValidadeLista(lista):
        print("Obs.: lista inválida")
    else:
        print("Obs.: lista válida")
        
    print("insira a opção que corresponde à rotina do Processual_
          "que receberá os números")
    op = 0
    while (op != 7):
        print("arquivo: " + fileProcessos + "\n")
        print("1 - mala direta")
        print("2 - movimentação")
        print("3 - localização")
        print("4 - verifica validade dos números")
        print("5 - alterar conteúdo do arquivo.")

        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            insertOracleMalaDireta(lista)   # inserir processos do arquivo para os
                                            # campos da rotina de mala direta
                                            # (PJFVA1516)
        elif op == 2:
            insertOracleMovimentacao(lista) # inserir processos do arquivo para os
                                            # campos da rotina de uma movimentação
                                            # para vários processos
                                            # (PJFVA1225)
        elif op == 3:
            insertOracleLocalizacao(lista)  # inserir processos do arquivo para os
                                            # campos da rotina de localização de
                                            # processos
                                            # (PJFVA1223)
        elif op == 4:
            if verificaValidadeLista(lista): 
                                             
               print("lista válida")
            else:
               print("lista inválida")
        elif op == 5:
            sanitizeFile(lista)
            print("feito")

        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()

