# -*- coding: utf-8 -*-

import os
import dividir
import shutil

#biblioteca para leitura do arquivo .pdf
from PyPDF2 import PdfFileReader
#biblioteca para modificação do arquivo .pdf
from PyPDF2 import PdfFileWriter
from pathlib import Path

#Para renomear o arquivo que possui espaços:
#------------------------------------------
#inputFormated = input_file.replace(" ","")
#print(inputFormated)
#os.rename(input_file, inputFormated)
#------------------------------------------

#reduzir tamanho do arquivo usando CPDF
#------------------------------------------
#def comprimir(input_file,output_file)
#   os.system("cpdf -compress "+input_file+" -o "+output_file)
#------------------------------------------
def reduzirCPDF(input_file,output_file):
    os.system("cpdf -compress " + input_file + " -o " + output_file)
    print("cpdf ok")

#reduzir tamanho do arquivo usando PDFSIZEOPT
#------------------------------------------
#os.chdir("c:/pdfsizeopt")
#print(os.getcwd())
#os.system("dir")
#os.system("pdfsizeopt "+input_file+" "+output_file)
#------------------------------------------
def reduzirPDFSIZEOPT(input_file,output_file):
    workingDirectory = os.getcwd() 
    os.chdir("d:/pdfsizeopt")
    #print(os.getcwd())
    #os.system("dir")
    os.system("pdfsizeopt " + input_file + " " + output_file)
    os.chdir(workingDirectory)
    print("pdfsizeopt ok")

#reduzir tamanho do arquivo usando GHOSTSCRIPT
#------------------------------------------
#gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=PDFComprimido.pdf PDFOriginal.pdf
#------------------------------------------ 
def reduzirGS(input_file,output_file):
    os.system("gswin64c -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=" + output_file + " " + input_file)
    print("gs ok")


def reduzirTamanhoArquivos(myPath):

#salvar arquivos que devem ser reduzidos em uma lista
#(e, no futuro, em um arquivo)
#listar os arquivos que tem tamanho maior que 10MB
    listaArquivos = []
    for folderName, subfolders, filenames in os.walk(myPath):
        for filename in filenames:
            pathArquivo = folderName+"\\"+filename
            if os.path.getsize(pathArquivo) > TAM:
    #            print(pathArquivo+": "+str(tamanho))
                listaArquivos.append(pathArquivo)
    #print(*listaArquivos,sep = "\n")
    #print(*a, sep = "\n") 



    #com a lista de arquivos criada, proceder às providências em toda a lista.
    for arquivo in listaArquivos:


        #print(arquivo+"("+str(os.path.getsize(arquivo))+")"+"\n")

        #criar pasta de backup
            #criar path da pasta
        pathPastaBkp = os.path.dirname(arquivo)+"\\bkp"
        print("caminho da pasta bkp: " + pathPastaBkp)
        #    verificar se a pasta existe
        #     em caso negativo, criá-la
        if os.path.exists(pathPastaBkp) == False:
            os.mkdir(pathPastaBkp)

        #criar cópia do arquivo nessa pasta
        #print("comando de cópia: copy " + arquivo + " " + pathPastaBkp+"\\")
        #os.system('copy ' + arquivo + ' ' + pathPastaBkp+"\\")
        #utilizar o shell não é o ideal, pois o comando não lida com os espaços existentes entre os nomes

#import shutil

#original = r'original path where the file is currently stored\file name.file extension'
#target = r'target path where the file will be copied\file name.file extension'

#shutil.copyfile(original, target)
#        shutil.copyfile

        original = arquivo
        nomeArquivo = os.path.basename(arquivo)
        target = pathPastaBkp+"\\"+nomeArquivo
        shutil.copyfile(original,target)



def otimiza(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        if len(subfolders)==0:
            if len(filenames)==0:
                print("pasta vazia")
            else:
                for file in filenames:
                    tamanho = os.path.getsize(folderName+"\\"+file)
                    print("arquivo: "+folderName[-43:]+"\\"+file)
                    strTamanho = str(tamanho)
                    print(" tamanho: "+strTamanho)
                    if tamanho > 10485760:
                        print("maior que 10MB\nComprimindo...")
                        inputFile = folderName + "\\" + file                        
                        #apaga arquivo dividido. por segurança, é preciso implementar uma rotina try except                        
                        try:
                            dividir.dividirAoMeio(inputFile)
                        except:
                            print("não foi possível dividir o arquivo")
                        else:
                            os.remove(inputFile)
                        
        else:
            for subfolder in subfolders:
                print(subfolder)
                otimiza(folderName+'\\'+subfolder)





def main():    
    op = 0
    while (op != 7):
        print("1 - ...")
        print("2 - ...")
        print("3 - ...")
        print("4 - ...")
        print("5 - ...")
        print("6 - ...")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 2:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 3:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 4:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 5:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 6:
            caminho = input("indique o caminho dos arquivos: ")
            
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
