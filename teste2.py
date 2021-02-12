# -*- coding: utf-8 -*-

import os
#biblioteca para leitura do arquivo .pdf
from PyPDF2 import PdfFileReader
#biblioteca para modificação do arquivo .pdf
from PyPDF2 import PdfFileWriter
from pathlib import Path


def renomearArquivos(myPath):
    listaArquivos = []
    listaArquivosNosDiretorios = []
    for folderName, subfolders, filenames in os.walk(myPath):
        for filename in filenames:
            listaArquivosNosDiretorios.append(folderName+"\\"+filename)

    for e in listaArquivosNosDiretorios:
        print(e)
    #print(filenames)
        #for filename in filenames:
         #   print(filename)
            #print(folderName+"\\"+filename)
        
        
#        for filename in filenames:
#            pathArquivo = folderName+"\\"+filename
#            if os.path.getsize(pathArquivo) > TAM:
#              print(pathArquivo+": "+str(tamanho))
#                listaArquivos.append(pathArquivo)





#D:\python\pasta_teste

def main():
    
    caminho = input("diretório: ")
    #print("valor informado: " + caminho)
    renomearArquivos(caminho)

    
if __name__ == "__main__":
    main()

