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

file = "D:\\file.txt"


def inserirNosCampos(processo):
    pyperclip.copy(processo)
    pyautogui.hotkey('ctrl','v')
    #pyperclip.paste
    pyautogui.press('tab')
    pyautogui.PAUSE = 0.5
    
    return 0

def insertOracleMalaDireta():
    lista = listGenerator()
    pyautogui.moveTo(164,180,0.2)
    pyautogui.click()
    if verificarValidade(lista):
       exit
    else:
        for processo in lista:
            inserirNosCampos(processo)
    return 0

def insertOracleMovimentacao():
    return 0

def insertOracleLocalizacao():
    return 0


def formatProcNumber(proc):
    procInvalido = False

    '''research stackoverflo(w).com
    >>> ok = "0123456789abcdef"
    >>> all(c in ok for c in "123456abc")
    True
    >>> all(c in ok for c in "hello world")
    False

    good = set('1234567890^-+x')

    if set(input_string) <= good:
        # it's good
    else:
        # it's bad
    '''
    #remove mask:
    if ("." in proc):
        proc.replace(".","")
    if ("-" in proc):
        proc.replace("-","")
            
    #tamanho da string proc
    if (len(proc) > 20):
        print("tamanho do número do processo é inválido")
        proc += "E"
        
    #caracteres válidos:
    validCharSet = set('1234567890.-')
    if not set(proc) <= validCharSet :
        print(proc + " possui caracteres inválidos...")
        procInvalido = True
        #é inserido um caractere no início da string do processo para informar que é inválido,
        #e a rotina que irá tratar a string saberá através dessa informação
            #my_string = "Python"
            #add_string = " is famous"
            #my_string += add_string
            #print("The string is : " + my_string)
        proc += "E"


            
    #format to have 20 characters
    if (len(proc) < 20) & (not procInvalido):
        if len(proc) < 20:
            quantZerosEsquerda = (20 - len(proc))*"0"
            proc = quantZerosEsquerda + proc

    return proc

def verificaValidadeProcesso(proc): #proc do tipo string

    valido = False
    #formata o número para que tenha 20 dígitos e seja retirada a máscara, se houver
    #Ex.: 100-15.2008.4.01.0000 -> 00001001520084010000
    
    formatedProcNumber = formatProcNumber(proc)
    print(erro inserido: formatedProcNumber[0])
    
    if not(formatedProcNumber[0] == "E"):
        
        #isola dígito

        #NNNNNNN-DD.AAAA.JTR.OOOO
        
        #Inicialmente, os dígitos verificadores D1 D0 devem ser deslocados para o final do número do processo e receber valor zero: 
        #   N6 N5 N4 N3 N2 N1 N0 A3 A2 A1 A0 J2 T1 R0 O3 O2 O1 O0 01 00

        

        #00001001520084010000 -> 00001002008401000000
        #isola primeiro caractere do dígito(D1). Verifica se é zero.
        ''' d1IsZero = False
        d2IsZero = False
        d1 = int(formatedProcNumber[7])
            if d1 == 0:
                d1IsZero = True
        #isola segundo caractere do dígito(D2)
        d2 = int(formatedProcNumber[8])
            if d2 == 0
                d2IsZero = True'''
        #desloca o dígito para o final do número

        #digito em string
        print(formatedProcNumber[7] + formatedProcNumber[8])
        digito = formatedProcNumber[7] + formatedProcNumber[8]
        intDigito = int(digito) 
        
        #formata número para cálculo do módulo, ou seja
        #retira o dígito e inclui dois zeros ao final do número
        proc = proc[:7] + proc[9:] + "00"

        print("rotina verValidade. parâmetro processo: ")
        print(proc)
        print("formatado: ")
        print(formatedProcNumber)
        
        np = int(formatedProcNumber) #transforma o número do processo para o tipo inteiro

        # verifica se a condição é atendida, ou seja
        # se 98 menos o módulo entre o np e 97 é igual ao dígito.
        # se for igual, o número do processo é válido.
        modulo = np % 97
        if (98-modulo == intDigito):
            valido = True
        
    return valido


#TRF da 1ª Região  NNNNNNN-DD.AAAA.JTR.OOOO 0000100-15.2008.401.0000 ou 100-15.2008.4013

#O cálculo dos dígitos verificadores (DD) da numeração única dos processos deve ser efetuado pela aplicação do algoritmo Módulo 97 Base 10, conforme Norma ISO 7064:2003, de acordo com as seguintes instruções: 
#I – Todos os campos do número único dos processos devem ser considerados no cálculo dos dígitos verificadores;  
#II – Inicialmente, os dígitos verificadores D1 D0 devem ser deslocados para o final do número do processo e receber valor zero:

#       N6 N5 N4 N3 N2 N1 N0 A3 A2 A1 A0 J2 T1 R0 O3 O2 O1 O0 01 00

#III – Os dígitos de verificação D1 D0 serão calculados pela aplicação da seguinte fórmula, na qual “módulo” é a operação “resto da divisão inteira”:

#       D1 D0 = 98 – (N6 N5 N4 N3 N2 N1 N0 A3 A2 A1 A0 J2 T1 R0 O3 O2 O1 O0 01 00 módulo 97) 

#IV - O resultado da fórmula deve ser formatado em dois dígitos, incluindo o zero à esquerda, se necessário. Os dígitos resultantes são os dígitos verificadores, que devem ser novamente deslocados para a posição original

#       (NNNNNNNDD.AAAA.JTR.OOOO).

#V – No caso de limitação técnica de precisão computacional que impeça a aplicação da fórmula sobre a integralidade do número do processo em uma única operação, pode ser realizada a sua fatoração, nos seguintes termos: 

#       R1 = (N6 N5 N4 N3 N2 N1 N0 módulo 97)
#       R2 = ((R1 concatenado com A3 A2 A1 A0 J2 T1 R0) módulo 97) 
#       R3 = ((R2 concatenado com O3O2O1O0 01 00) módulo 97) 
#   D1 D0 = 98 - R3 

#VI – A verificação da correção do número único do processo deve ser realizada pela aplicação da seguinte fórmula, cujo resultado deve ser igual a 1 (um):

#       N6 N5 N4 N3 N2 N1 N0 A3 A2 A1 A0 J2 T1 R0 O3 O2 O1 O0 D1D0 módulo 97 


def verificaValidadeLista(listv):

    #retorna falso se for encontrado algum número de processo com erro

    erro = False

    for processo in listv:
        #remove mask from process number, before call verificaValidadeProc()
        #proc = removeMask(processo)
        
        if verificaValidadeProcesso(processo):
            print("nº " + processo + " é válido")
            
        else:
            print("nº " + processo + " NÃO é válido")
            erro = True
            
    return erro

def listGenerator():
    with open(file) as f:
        lines = f.read().splitlines()
    return lines 

def main():
    print("insira a opção que corresponde à rotina que receberá os números")
    op = 0
    while (op != 7):
        print("1 - mala direta")
        print("2 - movimentação")
        print("3 - localização")
        print("4 - verificar se números dos processos são válidos")
 #       print("5 - ...")
 #       print("6 - ...")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            insertOracleMalaDireta()
        elif op == 2:
            insertOracleMovimentacao()
            pass
        elif op == 3:
            insertOracleLocalizacao()
            pass
        elif op == 4:
            lista = listGenerator()
            verificaValidadeLista(lista)
            pass
#        elif op == 5:
#            caminho = input("indique o caminho dos arquivos: ")
#            pass
#        elif op == 6:
#            caminho = input("indique o caminho dos arquivos: ")
#            pass
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()

