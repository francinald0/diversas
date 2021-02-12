#biblioteca para leitura do arquivo .pdf
from PyPDF2 import PdfFileReader
#biblioteca para modificação do arquivo .pdf
from PyPDF2 import PdfFileWriter

from pathlib import Path
import os

#---lista de funções---
#def nameFirstHalf(file):
#def nameSecondHalf(file):
#def cutFile(inputFile):
#def dividirArquivos(myPath):



def nameFirstHalf(file):
    name = file[:-4] + "_1.pdf"
    return name

def nameSecondHalf(file):
    name = file[:-4] + "_2.pdf"
    return name

def cutFile(inputFile):
    print("recebido pela rotina cutFile como: \n")
    print(inputFile)
    input_pdf = PdfFileReader(inputFile)
    pdf_writer1 = PdfFileWriter()
    pdf_writer2 = PdfFileWriter()

    numPages = input_pdf.getNumPages()
    if ((numPages % 2)==0):
        parte1 = numPages/2
    else:
        parte1 =(numPages+1)/2

    #indice=0
    for page in input_pdf.pages[:int(parte1)]:
        pdf_writer1.addPage(page)
        #print("page "+ str(indice+1)+" done")
        #indice = indice + 1

    arquivo_saida1 = nameFirstHalf(inputFile)
    print("nome do arquivo da primeira metade: \n")
    print(arquivo_saida1)
    with Path(arquivo_saida1).open(mode="wb") as output_file:
        pdf_writer1.write(output_file)
        #print("done")

    #indice=0
    for page in input_pdf.pages[int(parte1):]:
        pdf_writer2.addPage(page)
        #print("page "+ str(indice+1)+" done")
        #indice = indice + 1
    arquivo_saida2 = nameSecondHalf(inputFile)
    print("nome do arquivo da segunda metade: \n")
    print(arquivo_saida2)
    with Path(arquivo_saida2).open(mode="wb") as output_file:
        pdf_writer2.write(output_file)
        #print("done")
    
#TAM = 10485760 #10MB
#TAM = 2097152 #2MB
def dividirArquivos(myPath):
    print("valor recebido pela rotina:" + myPath)
    print("início da rotina dividirArquivos...\n")
    
    listaArquivosDividir = []
    indice = 0
    for folderName, subfolders, filenames in os.walk(myPath):
        if folderName[-3:] <> "bkp" #verificar
        for filename in filenames:
            pathArquivo = folderName+"\\"+filename
            print("índice: " + str(indice)+"\n")
            print("arquivo: " + pathArquivo + "\n")
            print("o arquivo deve ser dividido?: ")
            if os.path.getsize(pathArquivo) > TAM:
                listaArquivosDividir.append(pathArquivo)
                print("sim\n")
                print("arquivo adicionado à lista listaArquivosDividir\n\n\n")
            else:
                print("não\n\n\n")
            print("próximo arquivo...")
            indice = indice + 1
    os.system("pause")
    print("foram adicionado um total de" + str(indice) + "arquivos à lista")
    print("o comando len(listaArquivosDividir) retorna: " + str(len(listaArquivosDividir)))
    print("...agora, os arquivos da lista serão divididos")
    os.system("pause")
    for file in listaArquivosDividir:
        print("primeiro arquivo a ser dividido: ")
        print(file)
        if os.path.exists(file):
            print("arquivo existe.")
            cutFile(file)

            primeiraMetadeArquivo = nameFirstHalf(file)
            print("nome do arquivo da primeira metade gerado pela função nameFirstHalf: ")
            print(primeiraMetadeArquivo)

            segundaMetadeArquivo = nameSecondHalf(file)
            print("nome do arquivo da segunda metade gerado pela função nameSecondHalf: ")
            print(segundaMetadeArquivo)
            
            if os.path.getsize(primeiraMetadeArquivo) > TAM:
                listaArquivosDividir.append(primeiraMetadeArquivo)
            if os.path.getsize(segundaMetadeArquivo) > TAM:
                listaArquivosDividir.append(segundaMetadeArquivo)

            os.remove(file)
        listaArquivosDividir.remove(file)
    print("verificar se a rotina está vazia...")
    print("resultado do comando len(listaArquivosDividir): " + str(len(listaArquivosDividir)))
    print("resultado do if...")
    if listaArquivosDividir: #verifica se a lista está vazia
        print("não está vazia")
        r =input("deseja encerrar a execução?(s/n)")
        if r == s:
            exit
        dividirArquivos(myPath)
    else:
        print("está vazia")


def main():    
    op = 0
    while (op != 7):
        print("1 - nameFirstHalf(file)")
        print("2 - nameSecondHalf(file)")
        print("3 - cutFile(inputFile)")
        print("4 - dividirArquivos(myPath)")
        print("5 - ...")
        print("6 - ...")
        print("7 - Sair")
        op = int(input("Escolha a opção: "))
        
        if op == 1:
            arquivo = input("arquivo(caminho completo): ")
            print(nameFirstHalf(arquivo))
        elif op == 2:
            arquivo = input("arquivo(caminho completo): ")
            print(nameSecondHalf(arquivo))
        elif op == 3:
            arquivo = input("arquivo(caminho completo): ")
            cutFile(arquivo)
        elif op == 4:
            caminho = input("indique o caminho da pasta raiz: ")
            dividirArquivos(caminho)
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            exit
        else:
            print("opção inválida\n" + "op = " + str(op))

if __name__ == "__main__":
    main()


'''
def dividirAoMeio(inputFile):
    #verifica se a barra do caminho fornecido em
    #inputFile está para a direita. Caso estaja para a
    #esquerda, substitui por barra para a direita
    if '\\' in inputFile:
        inputFile = inputFile.replace('\\','/')
    #print(inputFile)

    #extrair nome do arquivo
    if '/' in inputFile:
        encontrou = False
        ultimo = len(inputFile)-1
        while not encontrou:
            if inputFile[ultimo]== '/':
                nomeArquivo = inputFile[ultimo+1:]
                nomePasta = inputFile[:ultimo+1]
                encontrou = True
            else:
                ultimo = ultimo - 1
    print("nome do arquivo: " + nomeArquivo)
    print("nome da pasta: " + nomePasta)
    destino1 = nomePasta+nomeArquivo[:-4]+"_1.pdf"
    destino2 = nomePasta+nomeArquivo[:-4]+"_2.pdf"
    print(destino1)
    print(destino2)


    input_pdf = PdfFileReader(inputFile)
    pdf_writer = PdfFileWriter()
    pdf_writer2 = PdfFileWriter()

    numPages = input_pdf.getNumPages()

    if ((numPages % 2)==0):
        parte1 = numPages/2
    else:
        parte1 =(numPages+1)/2
    indice=0
    for page in input_pdf.pages[:int(parte1)]:
        pdf_writer.addPage(page)
        print("page "+ str(indice+1)+" done")
        indice = indice + 1
    with Path(destino1).open(mode="wb") as output_file:
        pdf_writer.write(output_file)
        print("done")
    indice=0
    for page in input_pdf.pages[int(parte1):]:
        pdf_writer2.addPage(page)
        print("page "+ str(indice+1)+" done")
        indice = indice + 1
    with Path(destino2).open(mode="wb") as output_file:
        pdf_writer2.write(output_file)
        print("done")

    #cria pasta 'old' para armazenar o arquivo que foi dividido
    #para fins de backup, copiando-o em seguida
    #verificar primeiro, se o nome do arquivo possui espaços em branco
    #se positivo, ele deve ser colocado entre aspas. Deve-se ainda inverter
    #as barras, pois o comando "move" exige que as barras estejam invertidas.

    if " " in nomeArquivo:
        nomeArquivo = "\"" + nomeArquivo +"\""

    if os.path.isdir(nomePasta+"old"):
        print("old folder already exists in "+ nomePasta+". Moving divided file...")
        comandoBarrasInvertidas = 'move '+nomePasta+nomeArquivo+' '+nomePasta+"old/"+nomeArquivo
        comandoBarrasInvertidas = comandoBarrasInvertidas.replace('/','\\')
        os.system(comandoBarrasInvertidas)
        print(comandoBarrasInvertidas)
        print("done")
    else:
        print("old folder don\'t exists in " +nomePasta+". Creating...")
        os.mkdir(nomePasta+"old")
        print("done")
        print("Now, moving divided file...")
        comandoBarrasInvertidas = 'move '+nomePasta+nomeArquivo+' '+nomePasta+"old/"+nomeArquivo
        comandoBarrasInvertidas = comandoBarrasInvertidas.replace('/','\\')
        os.system(comandoBarrasInvertidas)
        print("done")
        
   
#caminho = input("arquivo, com caminho completo: ")
#dividirAoMeio(caminho)                          


#dividir arquivo ao meio
pdf_path = "D:/python/pasta_teste/2/Apostila Completa - Curso Renato Saraiva OAB (1).pdf"

input_pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()
pdf_writer2 = PdfFileWriter()

numPages = input_pdf.getNumPages()
#print(numPages)

if ((numPages % 2)==0):
    parte1 = numPages/2
else:
    parte1 =(numPages+1)/2
indice=0
for page in input_pdf.pages[:int(parte1)]:
    pdf_writer.addPage(page)
    print("page "+ str(indice+1)+" done")
    indice = indice + 1
with Path("D:/python/pasta_teste/parte1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
indice=0
for page in input_pdf.pages[int(parte1):]:
#for page in input_pdf.pages[5:9]:
    pdf_writer2.addPage(page)
    print("page "+ str(indice+1)+" done")
    indice = indice + 1
with Path("D:/python/pasta_teste/parte2.pdf").open(mode="wb") as output_file:
    pdf_writer2.write(output_file)


pdf_path = "caminho do arquivo"

#criação do objeto pdf, da classe PdfFileReader
#que faz a leitura do arquivo .pdf
pdf = PdfFileReader(str(pdf_path))
first_page = pdf.getPage(0) # atribui ao objeto a primeira página do arquivo lido

#print(pdf.getNumPages()) --> retorna o número de páginas
#print(pdf.documentInfo.title) -->  retorna o título do documento

#criação de um objeto que representa um pdf em branco, para receber
#as páginas e/ou alterações que se fizer em outro arquivo .pdf,
#no caso, do objeto pdf, da classe PdfReader
pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page) #adiciona a primeira página do arquivo lido ao arquivo em branco

with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file) # salva o arquivo no disco

#para adicionar 4 páginas do aquivo lido a um arquivo (pdf_out)
pdf_out = PdfFileWriter()
for n in range(1,4):
    page = pdf.getPage(n)
    pdf_out.addPage(page)

with Path("arquivo_final").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
        

#para adicionar um segmento de páginas

input_pdf = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in input_pdf.pages[1:4]:
    pdf_writer.addPage(page)

with Path("primeira parte.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

#page = pdf_writer.addBlankPage(width=72, height=72)

#print(type(page))

#with Path("blank.pdf").open(mode="wb") as output_file:
#    pdf_writer.write(output_file)


