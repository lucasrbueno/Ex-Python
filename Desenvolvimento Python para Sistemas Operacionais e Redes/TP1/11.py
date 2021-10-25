import os

input_arquivo = input("Qual arquivo de texto quer abrir? ")
arquivo = "notepad.exe " + input_arquivo

os.system(arquivo)