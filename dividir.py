#biblioteca para leitura do arquivo .pdf
from PyPDF2 import PdfFileReader
#biblioteca para modificação do arquivo .pdf
from PyPDF2 import PdfFileWriter

from pathlib import Path
'''
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

'''

#dividir arquivo ao meio
pdf_path = "C:/python/estudos/teste/Manual de Elaboração do Artigo.pdf"

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
with Path("C:/python/estudos/teste/parte1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
indice=0
for page in input_pdf.pages[int(parte1):]:
#for page in input_pdf.pages[5:9]:
    pdf_writer2.addPage(page)
    print("page "+ str(indice+1)+" done")
    indice = indice + 1
with Path("C:/python/estudos/teste/parte2.pdf").open(mode="wb") as output_file:
    pdf_writer2.write(output_file)










'''
#page = pdf_writer.addBlankPage(width=72, height=72)

#print(type(page))

#with Path("blank.pdf").open(mode="wb") as output_file:
#    pdf_writer.write(output_file)




#pdf_path vai armazenar o caminho do arquivo

def main():
    pdf_path = dir1+"1/catalogo telefone sjpi-sede-subsecoes.pdf"
#    pdf_path = (
#        Path.home()
#        /dir1+"/1/catalogo telefone sjpi-sede-subsecoes.pdf"
#    )
    #print(pdf_path)


# Calling main() function 
main() '''
