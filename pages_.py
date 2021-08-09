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

def desenhaPastas():
    print("renomeia os arquivos da pasta raíz para o padrão cnj")
    print("os arquivos devem ter a seguinte organização:")
    print("             Pasta raiz")
    print("                |")
    print("                |__processo1")
    print("                |     |__volume 1")
    print("                |     |      |__parte1.pdf")
    print("                |     |      |__ ...")
    print("                |     |__volume 2")
    print("                |     |      |__parte1.pdf")
    print("                |     |      |__parte2.pdf")
    print("                |     |      |__ ...")
    print("                |     |__ ...")         
    print("                |")
    print("                |__processo2")
    print("                |      |__ ...")
    print("                |")
    print("                |__processo3")
    print("                |      |__ ...")
    print("                |")
    print("                |")
    print("                |__ ...")

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


def verificaProcessos(myPath):
    listaDeProcessos = listdir(myPath)
    for processo in listaDeProcessos:
        if verValidade(processo):
            print("o processo "+processo+" é válido")
        else:
            print("o processo "+processo+" não é válido")
    

def renomearArquivos(myPath):
#renomeia os arquivos da pasta raíz para o padrão cnj
#os arquivos devem ter a seguinte organização:
#             Pasta raiz
#                |
#                |__processo1
#                |     |__volume 1
#                |     |      |__parte1.pdf
#                |     |      |__ ...
#                |     |__volume 2
#                |     |      |__parte1.pdf
#                |     |      |__parte2.pdf
#                |     |      |__ ...
#                |     |__ ...                  
#                |       
#                |__processo2
#                |      |__ ...
#                |
#                |__processo3
#                |      |__ ...
#                |
#                |
#                |__ ...
    desenhaPastas()
    print("Será verificada a validade do número dos processos indicados na pasta.")
    resposta = input("Deseja continuar(S/n):")
    if resposta == "n":
        exit
    else:
        verificaProcessos(myPath)
    
    print("O nome do processo da pasta raiz será modificado para que tenha 20 caracteres")
    resposta = input("Deseja continuar(S/n):")
    if resposta == "n":
        exit
    else:
        renomeiaPastasRaiz(myPath)
          
    print("Os arquivos da subpasta terão o nome alterado para o padrão da Migração")
    resposta = input("Deseja continuar(S/n):")
    if resposta == "n":
        exit
    else:
        renomeia_cnj(myPath)                         
                
def renomeia_cnj(myPath):
    numArquivosPath = int(len(listdir(myPath)))
    #print("número de diretórios na pasta indicada: " + str(numArquivosPath))
    listaDeProcessos = listdir(myPath)
    #print("diretórios da pasta: ")
    #print("--------------------início--------------------")
    #print(listaDeProcessos)                                


    for processo in listaDeProcessos:
        #print("processo nº: " + processo)
        
        pathProcessoAtual = os.path.join(myPath, processo)  #caminho completo da pasta do processo
        #print("processo atual: " + processo)


        listaDeArquivos = listdir(pathProcessoAtual) #lista dos arquivos dentro do processo
        
        #print("lista de arquivos dentro do processo:")
        #print(listaDeArquivos)

        for arquivo in listaDeArquivos: 
            
            if arquivo[:3] == "vol": #se é um volume...
                print("-----------------dentro do volume " + arquivo + "-----------------------")
                pathVolumeAtual = os.path.join(pathProcessoAtual, arquivo) #caminho completo da pasta do volume
                #print("tipo: volume")
                #print("volume atual: " + arquivo)

                
                #extrair o número do volume, que é o último caractere do nome
                penultimo = len(arquivo)-1
                numVolume = arquivo[penultimo:]

                listaDePartes_volume = listdir(pathVolumeAtual)#lista de arquivos dentro do diretório do volume

                for parte_volume in listaDePartes_volume:
                    
                    #print("arquivo: " + parte)

                    #rename com volume
                    #extrair o número do processo
                    
                    numProcesso = processo                                                      
    
                    #extrair o número da parte do arquivo segmentado
                    posNum = len(parte_volume)-5
                    #print("posicao na string " + str(posNum))
                    numParteArquivo = parte_volume[posNum]
                    #print("número extraído: " + str(numParteArquivo))

                    nomeAntigo = os.path.join(pathVolumeAtual, parte_volume)
                    nome = numProcesso + "_V00" + numVolume + "_00" + numParteArquivo + ".pdf"
                    nomeNovo = os.path.join(pathVolumeAtual, nome)


                    print("renomeando arquivo " + parte_volume + " dentro do volume " + numVolume)
                    print("nome antigo: " + nomeAntigo)
                    print("nome novo: " + nomeNovo)

                    r"{}".format(nomeAntigo)
                    r"{}".format(nomeNovo)

                    os.rename(nomeAntigo, nomeNovo)
                    

            else: #...senão é arquivo, com volume único
                
                
                listaDePartes_arquivo = listdir(pathProcessoAtual)
                for parte_arquivo in listaDePartes_arquivo:
                    #print("tipo: arquivo")
                    #print("arquivo: " + parte)

                    #rename volume único

                    #extrair o número do processo
                    numProcesso = processo
                    #extrair o número do volume
                    numVolume = "1"
                    #extrair o número da parte do arquivo segmentado

                    posNum = len(parte_arquivo)-5
                    #print("posicao " + str(posNum))
                    numParteArquivo = parte_arquivo[posNum]
                    #print("número extraído do nome: " + numParteArquivo)

                    nomeAntigo = os.path.join(pathProcessoAtual, parte_arquivo)
                    nome = numProcesso + "_V00" + numVolume + "_00" + numParteArquivo + ".pdf"
                    nomeNovo = os.path.join(pathProcessoAtual, nome)
                    
                    


                    print("renomeando arquivo " + parte_arquivo + " dentro do volume único")
                    print("nome antigo: " + nomeAntigo)
                    print("nome novo: " + nomeNovo)

                    r"{}".format(nomeAntigo)
                    r"{}".format(nomeNovo)
                    #r"{}".format(string)
                    os.rename(nomeAntigo, nomeNovo)        





#acrescenta zeros à esquerda do nome da pasta, para que ele tenha 20 dígitos
def renomeiaPastasRaiz(myPath):
    for count, filename in enumerate(os.listdir(myPath)):
        zeros = "" 
        if os.path.isdir(myPath+"\\"+filename):
            nomePasta = filename
            tamanhoNomePasta = len(filename)
            while (tamanhoNomePasta<=19):
               zeros = "0"+zeros
               tamanhoNomePasta = tamanhoNomePasta + 1
            src = myPath +"\\"+ filename
            dst = myPath +"\\"+ zeros + nomePasta
            os.rename(src, dst)
            


#def renomearArquivos(myPath):
#def renomeia_cnj(myPath):
#def renomeiaPastasRaiz(myPath):

def main():    
    op = 0
    while (op != 7):
        print("1 - assistente")
        print("2 - renomeia_cnj (renomeia os arquivos da pasta indicada para o padrão CNJ")
        print("3 - renomeiaPastaRaiz (nome da pasta é acrescido de zeros à esquerda")
        print("4 - verificar se números dos processos são válidos")
 #       print("5 - ...")
 #       print("6 - ...")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("indique o caminho dos arquivos: ")
            renomearArquivos(caminho)
        elif op == 2:
            caminho = input("indique o caminho dos arquivos: ")
            renomeia_cnj(caminho)
            pass
        elif op == 3:
            caminho = input("indique o caminho dos arquivos: ")
            renomeiaPastasRaiz(caminho)
            pass
        elif op == 4:
            caminho = input("indique o caminho dos arquivos: ")
            verificaProcessos(caminho)
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

    #C:\python\teste
