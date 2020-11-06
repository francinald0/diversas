#utiliza aplicação do console para otimizar arquivos em pdf

import os

input_file = "C:/python/estudos/teste/DataStructuresandAlgorithmsinPython.pdf"
output_file = "C:/python/estudos/teste/saida.pdf"

#Para renomear o arquivo que possui espaços:

#inputFormated = input_file.replace(" ","")
#print(inputFormated)
#os.rename(input_file, inputFormated)


os.chdir("c:/pdfsizeopt")
print(os.getcwd())
os.system("dir")
os.system("pdfsizeopt "+input_file+" "+output_file)




