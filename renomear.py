# Pythono3 code to rename multiple 
# files in a directory or folder 


# importing os module 
import os 


# constantes
dir1 = "d:/python/pasta_teste/"
dir2 = "W:\PROCESSOS DIGITALIZADOS 2020/"


'''
# Function to rename multiple files 
def main():
#print(os.listdir("d:/python/pasta_teste/"))
    for count, filename in enumerate(os.listdir(dir1)):
        dst = "000" + str(count) + ".txt"
        src = dir1 + filename
        dst = dir1 + dst
        os.rename(src, dst)
print("done")
# Driver Code 
#if __name__ == '__main__': 





def main():
    for count, filename in enumerate(os.listdir(dir1)):
        zeros = ""
        print("Before: name of file: " + filename + ", lenght: " + str(len(filename)))
        nomeArquivo = filename
        tamanhoNomeArquivo = len(filename)
        while (tamanhoNomeArquivo<=19):
           zeros = "0"+zeros
           tamanhoNomeArquivo = tamanhoNomeArquivo + 1
        src = dir1 + filename
        dst = dir1 + zeros + nomeArquivo
        #dst = dir2 + nomeArquivo[1:]
        os.rename(src, dst)
        print("After: name of file: " + filename + ", lenght: " + str(len(filename)))

#print(str(len(filename)) + " - " + str(count))
        


#file size

def main():
    for root, dirs, files in os.walk(dir1):
        for file in files:
            #print(os.walk(subdir))
            #print(os.path.join(subdir, file))
            print('nome: '+ file + ' tamanho: ' + str(os.path.getsize(os.path.join(root,file))))

            #+ str(os.path.getsize(os.path.join(subdir,file)))


        
    
  for root, dirs, files in os.walk(dir1):
        print(root, "consumes", end=" ")
        print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")'''




'''
for count, filename in enumerate(os.listdir(dir1)):
        if os.path.isdir(dir1+filename):
            print(filename + " is a directory")
            #print('its size is ' + str(os.stat(dir1+filename).st_size))
            print('its size is ' + str(os.path.getsize(dir1+filename)))
        else:
            print(filename + " is a file")
            #print('its size is ' + str(os.stat(dir1+filename).st_size))
            print('its size is ' + str(os.path.getsize(dir1+filename)))
'''

#pdf mod
'''    pdf = PdfFileReader(str(pdf_path))
    first_page = pdf.getPage(0)

    #print(pdf.getNumPages())
    #print(pdf.documentInfo.title)

    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(first_page)

    with Path("first_page.pdf").open(mode="wb") as output_file:
        pdf_writer.write(output_file)


    pdf_out = PdfFileWriter()
    for n in range(1,4):
        page = pdf.getPage(n)
        pdf_out.addPage(page)

    with Path("arquivo_final").open(mode="wb") as output_file:
        pdf_writer.write(output_file)
        
    #page = pdf_writer.addBlankPage(width=72, height=72)

    #print(type(page))

    #with Path("blank.pdf").open(mode="wb") as output_file:
    #    pdf_writer.write(output_file)'''
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

from pathlib import Path

#pdf_path vai armazenar o caminho do arquivo

def main():
    pdf_path = dir1+"1/catalogo telefone sjpi-sede-subsecoes.pdf"
#    pdf_path = (
#        Path.home()
#        /dir1+"/1/catalogo telefone sjpi-sede-subsecoes.pdf"
#    )
    #print(pdf_path)

    input_pdf = PdfFileReader(str(pdf_path))

    pdf_writer = PdfFileWriter()

    for page in input_pdf.pages[1:4]:
        pdf_writer.addPage(page)

    with Path("primeira parte.pdf").open(mode="wb") as output_file:
            pdf_writer.write(output_file)

# Calling main() function 
main() 









