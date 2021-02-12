# -*- coding: utf-8 -*-

import os 

def renomearArquivos(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        for filename in filenames:
            procName = myPath[-27:-8]
            mask = procName+"_v0"
            indice = len(filenames)
            for file in reversed(filenames):
                if indice >= 10:
                    os.rename(myPath+'\\'+file, myPath+'\\'+mask+"_0"+str(indice)+".pdf")
                else:
                    os.rename(myPath+'\\'+file, myPath+'\\'+mask+"0"+str(indice)+".pdf")
                indice = indice -1


def renomeia_cnj(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        #for file in reversed(filenames):
        #    print(file)   
        for subfolder in subfolders:
            print(subfolder)
            if subfolder[:6]=="volume":
                renomeia_arquivos(folderName+"\\"+subfolder)
            renomeia_cnj(folderName+'\\'+subfolder)


#renomeia somente as pastas da pasta raiz
def renomeiaPastasRaiz(myPath):
    for count, filename in enumerate(os.listdir(myPath)):
        zeros = "" 
        #print("Before: name of file: " + filename + ", lenght: " + str(len(filename)))
        if os.path.isdir(myPath+"\\"+filename):
            nomePasta = filename
            tamanhoNomePasta = len(filename)
            while (tamanhoNomePasta<=19):
               zeros = "0"+zeros
               tamanhoNomePasta = tamanhoNomePasta + 1
            src = myPath +"\\"+ filename
            dst = myPath +"\\"+ zeros + nomePasta
            os.rename(src, dst)


def renomearArquivos(myPath):
def renomeia_cnj(myPath):
def renomeiaPastasRaiz(myPath):

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
            pass
        elif op == 2:
            caminho = input("indique o caminho dos arquivos: ")
            pass
        elif op == 3:
            caminho = input("indique o caminho dos arquivos: ")
            pass
        elif op == 4:
            caminho = input("indique o caminho dos arquivos: ")
            pass
        elif op == 5:
            caminho = input("indique o caminho dos arquivos: ")
            pass
        elif op == 6:
            caminho = input("indique o caminho dos arquivos: ")
            pass
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()
