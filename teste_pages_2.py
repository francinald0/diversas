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
from datetime import date
from PyPDF2 import PdfFileReader


def PagesCountPDFFile(path):
    path = path.replace("\\","/")
    inputPdf = PdfFileReader(open(path, "rb"))
    pages = inputPdf.getNumPages()
    #print("O arquivo: " + path +" possui " + str(pages) + " páginas")
    return pages

#retorna informações sobre o número de páginas dos arquivos PDF

def pagesByProcess(path):

    numArquivosPath = int(len(listdir(path)))
    print("número de diretórios(processos) na pasta indicada: " + str(numArquivosPath))

    #lista de Processos é a lista que possui o nome dos diretórios existentes na pasta indicada, ora nomeados com o número do processo
    #cujos arquivos estão ali armazenados

    listaDeProcessos = listdir(path)

    sumOfAllPages = 0
    sumOfAllVols = 0
   
    #para cada diretório(processo), nessa lista de diretórios, faça:
    for processo in listaDeProcessos:
        volUnico = True

        print("Relatório do processo " + processo)
        
        pathProcessoAtual = os.path.join(path, processo)  #caminho completo do diretório(do processo)

        listaDeArquivos = listdir(pathProcessoAtual) #lista dos arquivos dentro do diretório(processo): pode ser de volumes de arquivos
                                                     #ou só arquivo
        firstFile = listaDeArquivos[0]

        volTotalOfProc = 1
        
        if firstFile[:3] == "vol":
            volUnico = False
            sumOfAllVols = sumOfAllVols + 1
            volTotalOfProc = 0
        
        pagesTotalperProcess = 1
        fileNumber = 1
        
        #para cada arquivo/diretório dentro do diretório(processo), faça:

        for arquivo in listaDeArquivos:
            
            #verifica se os arquivos do diretório do processo são arquivos ou subdiretórios
            if not volUnico:
            
                sumOfAllVols = sumOfAllVols + 1

                volTotalOfProc = volTotalOfProc + 1

                #caminho completo da pasta desse volume
                pathVolumeAtual = os.path.join(pathProcessoAtual, arquivo) 

                print("volume nº " + str(volTotalOfProc))
                
                #o path é setado para o diretório do processo

                #extrair o número do volume, que é o último caractere do nome desse diretório
                penultimo = len(arquivo)-1
                numVolume = arquivo[penultimo:]

                #################
                #pathVolumeAtual = pathVolumeAtual.replace(r"\\" , "/")
                ################

                listOfVolFiles = listdir(pathVolumeAtual) # lista de arquivos dentro do volume
                
                print("O volume nº " + numVolume)
                #print((len(listOfVolFiles)) " arquivos")

                

                #lista com os arquivos dentro do diretório do volume
                #extrair o número de páginas de cada arquivo PDF existente dentro do volume

                #para cada arquivo dentro do volume, faça:

                for fileInsideVol in listOfVolFiles:
                                    
                    #numProcesso = processo
                    #caminho completo do arquivo
                    pathFileProcesso = os.path.join(pathVolumeAtual, fileInsideVol)
                    
                    filePagesNumber = PagesCountPDFFile(pathFileProcesso)

                    print("O arquivo nº " + str(fileNumber) +" possui "+ str(filePagesNumber) + " páginas")

                    pagesTotalperProcess = pagesTotalperProcess + filePagesNumber

                    fileNumber = fileNumber + 1
                    

            else: #...senão é volume, é arquivo
              
                #fileListInsideProc = listdir(pathProcessoAtual)
                
                pathFileProcesso = os.path.join(pathProcessoAtual, arquivo)
                filePagesNumber = PagesCountPDFFile(pathFileProcesso)
                    
                pagesTotalperProcess = pagesTotalperProcess + filePagesNumber
                print("o arquivo " + str(fileNumber) + " possui "+ str(filePagesNumber) +" páginas")



                
        print("o processo possui um total de " + str(pagesTotalperProcess) + " páginas")
        print("o processo possui " + str(volTotalOfProc) + " volume(s)")
        print("o processo possui a média de " + str(pagesTotalperProcess/volTotalOfProc)+" páginas por volume")
        sumOfAllPages = sumOfAllPages + pagesTotalperProcess
        sumOfAllVols = sumOfAllVols + volTotalOfProc
                              
            



    processTotal = numArquivosPath
    volTotal = sumOfAllVols
    pagsTotal = sumOfAllPages

    pagsPerProcAverage = pagsTotal / processTotal
    pagsPerProcAverage = round(pagsPerProcAverage,2)
    
    pagsPerVolAverage = pagsTotal / volTotal
    pagsPerVolAverage = round(pagsPerVolAverage,2)

    volsPerProcAverage = volTotal / processTotal
    volsPerProcAverage = round(volsPerProcAverage,2)

    print("*******************************RELATÓRIO*******************************")

    print("TOTAL DE PROCESSOS " + str(processTotal))

    print("TOTAL DE VOLUMES " + str(volTotal))

    print("TOTAL DE PÁGINAS: " + str(pagsTotal))
    
    print("MÉDIA DE PÁGINAS POR PROCESSO " + str(pagsPerProcAverage))

    print("MÉDIA DE PÁGINAS POR VOLUME " + str(pagsPerVolAverage))

    print("MÉDIA DE VOLUMES POR PROCESSO " + str(volsPerProcAverage))

    print("DATA ATUAL " +  str(date.today()))
    

         
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

    caminho = input("informe o caminho completo do diretório: ")
        pagesByProcess(caminho)

    
if __name__ == "__main__":
    main()

   
