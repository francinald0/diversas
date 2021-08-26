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

from datetime import datetime





#now = datetime.now()
#now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#arquivo com lista de processos
ARQ_PROCESSOS = 'D:\scripts\docs\processos.txt'

def publicacao():
    opP = -1
    while (opP != 0):
        print("1 - DESPACHO")
        print("2 - DECISÃO")
        print("3 - SENTENÇA")
        print("4 - ATO ORDINATÓRIO")
        print("5 - Voltar")
        print("0 - Sair")
        opP = int(input("Opção: "))
        
        if opP == 1:
            print("opção escolhida: DESPACHO")
        elif opP == 2:
            print("opção escolhida: DECISÃO")
        elif opP == 3:
            print("opção escolhida: SENTENÇA")   
        elif opP == 4:
            print("opção escolhida: ATO ORDINATÓRIO")
        elif opP == 5:
            print("opção 5")
            break
        elif opP == 0:
            print("opção 0")
            exit
        else:
            #print("opção inválida\n" + "op = " + str(op))
            print("opção inválida\n")


        print("início: " + str(now))
            opP2 = -1
        while (opP2 != 0):
            print("1 - Transferir processos para Oracle")
            print("2 - Lançar movimentação nos processos")
            print("3 - ...")
            print("4 - ...")
            print("5 - Voltar")
            print("0 - Sair")
            opP = int(input("Opção: "))
            
            if opP2 == 1:
                print("executar inserir processos")
            elif opP2 == 2:
                print("executar movimentar_processos")
            elif opP2 == 3:
                print("")   
            elif opP2 == 4:
                print("")
            elif opP2 == 5:
                print("opção 5")
                break
            elif opP2 == 0:
                print("opção 0")
                exit
            else:
                #print("opção inválida\n" + "op = " + str(op))
                print("opção inválida\n")

            
    input("procedimento finalizado?(s/n): ")
    
    
    
def redistribuicao():
    print('')
    
def pjeRetificacao():
    print('')
    
def pjeRemessa():
    print('')
    
def pjeOutros():
    print('')
    
def auxilios():
    print('')

def main():

    op = -1
    while (op != 0):
        print("1 - publicação")
        print("2 - [pje] - redistribuição")
        print("3 - [pje] - retificação")
        print("4 - [pje] - remessa ao TRF1")
        print("5 - [pje] - outros")
        print("6 - auxílios")
        print("7 - ...")
        print("8 - ...")
        print("9 - ...")
        print("0 - Sair")
        op = int(input("Opção: "))
        
        if op == 1:
            print("opção 1")
            publicacao()
        elif op == 2:
            print("opção 2")
            redistribuicao()
        elif op == 3:
            print("opção 3")
            pjeRetificacao()
        elif op == 4:
            print("opção 4")
            pjeRemessa()
        elif op == 5:
            print("opção 5")
            pjeOutros()
        elif op == 6:
            print("opção 6")
            auxilios()
        elif op == 7:
            print("opção 7")
        elif op == 8:
            print("opção 8")
        elif op == 9:
            print("opção 0")
        elif op == 0:
            exit
            
        else:
            #print("opção inválida\n" + "op = " + str(op))
            print("opção inválida\n")


if __name__ == '__main__':
    main()
