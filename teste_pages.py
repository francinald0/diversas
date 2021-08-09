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

from PyPDF2 import PdfFileReader


def PagesCountPDFFile(path):
    inputPdf = PdfFileReader(open(path, "rb"))
    pages = inputPdf.getNumPages()
    #print("O arquivo: " + path +" possui " + str(pages) + " páginas")
    return pages

def AverageVolumes(path):
        return 0

#retorna o resultado obtido pela divisão entre o número total de páginas dos processos
#dividido por duzentos e o resultado dessa divisão deve ser dividido pelo número de processos.

def AverageCalc(path):
    return 0
#retorna resultado da divisão entre o número total de páginas e o número de processos

def totalPagesNumber(path):
    return 0
#retorna o número de páginas dos arquivos em pdf existentes no diretório indicado

def pagesByProcess(path):

#retorna o número total de páginas de cada processo

    numArquivosPath = int(len(listdir(path)))
    print("número de diretórios(processos) na pasta indicada: " + str(numArquivosPath))

    #lista de Processos é a lista que possui o nome dos diretórios existentes na pasta indicada, ora nomeados com o número do processo
    #cujos arquivos estão ali armazenados
    listaDeProcessos = listdir(path)

    sumOfAllPages = 0
    sumOfAllVols = 0
    
    #para cada diretório(processo), nessa lista de diretórios, faça:
    for processo in listaDeProcessos:

        print("Relatório do processo " + processo)
        
        pathProcessoAtual = os.path.join(path, processo)  #caminho completo do diretório(do processo)
        listaDeArquivos = listdir(pathProcessoAtual) #lista dos arquivos dentro do diretório(processo): pode ser de volumes de arquivos
                                                        #ou só arquivos
        
        #para cada arquivo/diretório dentro do diretório(processo), faça:
        
        for arquivo in listaDeArquivos:
            pagesTotalperProcess = 0
            volTotalOfProc = 0
            if arquivo[:3] == "vol": #se os arquivos/diretórios são nomeados como volumes...                
            
                pathVolumeAtual = os.path.join(pathProcessoAtual, arquivo) #caminho completo da pasta desse volume
                
                #extrair o número do volume, que é o último caractere do nome desse diretório
                penultimo = len(arquivo)-1
                numVolume = arquivo[penultimo:]

                listOfVolFiles = listdir(pathVolumeAtual) # lista de volumes do diretório
                
                print("O volume nº " +str(numVolume)+ " possui " + str(len(listdir(pathVolumeAtual))) + " arquivos")

                #lista com os arquivos dentro do diretório do volume
                #extrair o número de páginas de cada arquivo PDF existente dentro do volume
                
                sumOfAllVols = sumOfAllVols + 1
                
                fileNumber = 1

                #para cada volume, faça:
                for volFile in listOfVolFiles:
                                    
                    volTotalOfProc = volTotalOfProc + 1

                    #numProcesso = processo
 
                    pathFileProcesso = os.path.join(pathVolumeAtual, volFile)


                    #**************************************************************

                    filePagesNumber = PagesCountPDFFile(pathFileProcesso)

                    print("O arquivo nº " + str(fileNumber) +" possui "+ str(filePagesNumber) + " páginas")

                    pagesTotalperProcess = pagesTotalperProcess + filePagesNumber

                    fileNumber = fileNumber + 1
                    

                    #**************************************************************
                
                

            
            else: #...senão é arquivo, é volume único
                fileNumber = 1
                sumOfAllVols = sumOfAllVols + 1
                listaDePartes_arquivo = listdir(pathProcessoAtual)
                print("O volume único possui " + str(len(listaDePartes_arquivo)) + " arquivos")
                for parte_arquivo in listaDePartes_arquivo:

                    #extrair o número do processo
                    numProcesso = processo
                    
                    #extrair o número da parte do arquivo segmentado

                    #**************************************************************
                    pathFileProcesso = os.path.join(pathProcessoAtual, parte_arquivo)

                    filePagesNumber = PagesCountPDFFile(pathFileProcesso)
                    pagesTotalperProcess = pagesTotalperProcess + filePagesNumber

                    print("O arquivo nº " + str(fileNumber) + " possui " + str(filePagesNumber) + " páginas")

                    fileNumber = fileNumber + 1
                    #**************************************************************
                
                
            
                
        print("Número de páginas: " + str(pagesTotalperProcess))
        sumOfAllPages = sumOfAllPages + pagesTotalperProcess
        sumOfAllVols = sumOfAllVols + volTotalOfProc
    print("*******************************RELATÓRIO*******************************")
    print("TOTAL DE PÁGINAS: " + str(sumOfAllPages))
    print("PÁGINAS POR PROCESSO: " + str(sumOfAllPages/numArquivosPath))
    print("TOTAL DE VOLUMES " + str(sumOfAllVols))
    print("VOLUMES POR PROCESSO: " + str(sumOfAllVols/numArquivosPath))



def fileReportGenerator(caminho):
        return 0

#grava em arquivo as informações:

#média de páginas por processo
#média de volumes existentes
#média de volumes por processo
#número total de páginas
#número total de processos
#número total de volumes
#data do relatório

         
#grava lista de arquivos com nome de processo no diretório indicado

def extraiNomesArquivos(path): #retorna lista com o nome dos arquivos no diretório informado
    onlyFiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyFiles

def extraiNomesDiretorios(path): #retorna lista com o nome das pastas do diretório informado
    onlyDirs = [f for f in listdir(path) if isdir(join(path, f))]
    return onlyDirs

def gravaListaProcessos(path, option):
    if option == 1:
        listaDeProcessos = extraiNomesArquivos(path) #para extrair nome dos arquivos
    if option == 2:
        listaDeProcessos = extraiNomesDiretorios(path)#para extrair nome das pastas
    
    arquivo = open(path+"\lista.txt","a")
    for f in listaDeProcessos:
        #if "4" in f: #se tiver o número 4 no arquivo, é porque é um número de processo
        arquivo.write(f+"\n")
    arquivo.close()

  

def main():
    #caminho = "W:/FRANCINALDO/testes/00000035620164014000/00000035620164014000_V001_001.pdf"
    caminho = "d:/testes/"
    pagesByProcess(caminho)

    
if __name__ == "__main__":
    main()

   
