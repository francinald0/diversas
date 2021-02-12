# -*- coding: utf-8 -*-

import os
import shutil

#reduzir tamanho do arquivo usando CPDF
#------------------------------------------
#def comprimir(input_file,output_file)
#   os.system("cpdf -compress "+input_file+" -o "+output_file)
#------------------------------------------


#reduzir tamanho do arquivo usando PDFSIZEOPT
#------------------------------------------
#os.chdir("c:/pdfsizeopt")
#print(os.getcwd())
#os.system("dir")
#os.system("pdfsizeopt "+input_file+" "+output_file)
#------------------------------------------

#reduzir tamanho do arquivo usando GHOSTSCRIPT
#------------------------------------------
#gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=PDFComprimido.pdf PDFOriginal.pdf
#------------------------------------------

def reduzirCPDF(input_file,output_file):
    os.system("cpdf -compress " + input_file + " -o " + output_file)
    print("cpdf ok")

def reduzirPDFSIZEOPT(input_file,output_file):
    workingDirectory = os.getcwd() 
    os.chdir("d:/pdfsizeopt")
    #print(os.getcwd())
    #os.system("dir")
    os.system("pdfsizeopt " + input_file + " " + output_file)
    os.chdir(workingDirectory)
    print("pdfsizeopt ok")

def reduzirGS(input_file,output_file):

    os.system("gswin64c -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=" + output_file + " " + input_file)
    print("gs ok")
    
def reduzir(input_file,output_file):
    os.system("cpdf -compress " + input_file + " -o " + output_file)


    workingDirectory = os.path.getcwd() 
    os.chdir("c:/pdfsizeopt")
    #print(os.getcwd())
    #os.system("dir")
    os.system("pdfsizeopt " + input_file + " " + output_file)
    os.chdir(workingDirectory)

    os.system("gwin64c -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile=" + output_file + " " + input_file)


def removerPastasBkp(myPath):
    listaPastasBkp = []
    for folderName, subfolders, filenames in os.walk(myPath):
        #print(folderName)
        #print(folderName[-3:])
        if folderName[-3:]=="bkp":
            listaPastasBkp.append(folderName)
    for pasta in listaPastasBkp:
        shutil.rmtree(pasta)




#TAM = 10485760 #10MB
TAM = 200000 
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

        #print(os.path.dirname(arquivo)) --> imprime somente o caminho do arquivo
        #print(os.path.basename(arquivo)) --> imprime somente o nome do arquivo

        #gerar arquivo em pdf reduzido

        arquivoInicial = r'%s' %arquivo
        arquivoFinal = arquivoInicial[:-3]+"_r.pdf"

#test = 'C:\\Windows\Users\alexb\'
#rawtest = r'%s' %test

        
        reduzirCPDF(arquivoInicial,arquivoFinal)
        #reduzirPDFSIZEOPT(arquivoInicial,arquivoFinal)
        #reduzirGS(arquivoInicial,arquivoFinal)

        #remover arquivo de origem
        os.remove(arquivo)


#def dividirArquivos(myPath):



#def renomearArquivos(myPath):
















#--------------------------------------------------------------------------------------------------
#mostra todas as subpastas do diretório raiz
def navegarPastas0(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        print(folderName)

        
#--------------------------------------------------------------------------------------------------
#verifica quais são os subdiretórios e arquivos em cada uma das pastas do diretório raiz
def navegarPastas1(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        print("the current folder is " + folderName)
        os.system("pause")
#lista os subdiretórios
        if len(subfolders)==0: #verifica se existem subdiretórios
            print("não existem subdiretórios em " + folderName)
        else:
            print("os subdiretórios são: ")
            for subfolder in subfolders:
                print(subfolder)
#lista os arquivos
        if len(filenames)== 0:
            print("não existem arquivos em " + folderName)
        else:
            print("os arquivos são:")
            for filename in filenames:
                print(filename)
#--------------------------------------------------------------------------------------------------


def navegarPastas2(myPath):
        for folderName, subfolders, filenames in os.walk(myPath):
            #print(folderName)
            for filename in filenames:
                print(folderName+"\\"+filename)
                #print("nome: "+filename+"tamanho: "+os.stat(filename).st_size)
                #print(os.path.join(myPath,filename))
                #pathArquivo = os.path.abspath(filename)
                #tamanho = os.path.getsize(pathArquivo)
                #if tamanho > 10485760:
                    #print(filename + " maior que 10MB")


def verificaErros(myPath):
    for folderName, subfolders, filenames in os.walk(myPath):
        for filename in filenames:
            pathArquivo = folderName+"\\"+filename
            tamanho = os.path.getsize(pathArquivo)
            if tamanho == 0:
                print(pathArquivo+": "+str(tamanho))

            #print(folderName+"\\"+filename)
            #print("nome: "+filename+"tamanho: "+os.stat(filename).st_size)
            #print(os.path.join(myPath,filename))
            #pathArquivo = os.path.abspath(filename)
            #tamanho = os.path.getsize(pathArquivo)
            #if tamanho > 10485760:
                #print(filename + " maior que 10MB")

#renomeia somente as subpastas da pasta raiz
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


#lista arquivos de um determinado tipo

#import os
def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

#chamada:
# my_files_list = list_files(' C:\\Users\\Public\\Downloads', '.csv')



#diretório corrente: #pathArquivo = os.path.abspath(filename)
#tamanho do arquivo
#tamanho = os.path.getsize(folderName_l1+'\\'+subfolder_l1+'\\'+filename_l1)
#print('arquivo: ' + filename_l2 +', tamanho: ' + tamanho)

# mostrar todos os arquivos maiores que 10MB em uma árvore de diretórios
# if tamanho > 10485760:
#   print("maior que 10MB")

'''
def list_files(filepath):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.
            paths.append(os.path.join(root, file))
   return(paths)
'''


def retiraNumProc(myPath):    
    procName = myPath[-27:-8]
    print(procName)
    print(myPath)
    

#path = "D:\python\pasta_teste\procs\00061207320104014000\volume 1"
#retiraNumProc(path)
#print(path)


def main():
    
    op = 0
    while (op != 7):
        print("1 - navegarPastas0")
        print("2 - navegarPastas1")
        print("3 - navegarPastas2")
        print("4 - removerPastasBkp(myPath)")
        print("5 - renomeiaPastasRaiz")
        print("6 - reduzirTamanhoArquivos")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            caminho = input("indique o caminho dos arquivos: ")
            navegarPastas0(caminho)
        elif op == 2:
            caminho = input("indique o caminho dos arquivos: ")
            navegarPastas1(caminho)
        elif op == 3:
            caminho = input("indique o caminho dos arquivos: ")
            percorrerPastasMaiorQue10MB(caminho)
        elif op == 4:
            caminho = input("indique o caminho dos arquivos: ")
            removerPastasBkp(caminho)
        elif op == 5:
            caminho = input("indique o caminho dos arquivos: ")
            renomeiaPastasRaiz(caminho)
        elif op == 6:
            caminho = input("indique o caminho dos arquivos: ")
            reduzirTamanhoArquivos(caminho)
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))



if __name__ == "__main__":
    main()
