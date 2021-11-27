import os

# C:\\Users\\Lucas\\Desktop\\Exercicios-Python\\
diretorio = input("Qual diretório deseja obter os arquivos? ")

arquivos = []
tamanho = []
descrescente = []

for item in os.listdir(diretorio):
    if os.path.isfile(item):
        arquivos.append(item)
        tamanho.append(os.stat(item).st_size)

tamanho.sort(reverse=True)

for item in tamanho:
    for jtem in arquivos:
        if os.stat(jtem).st_size == item:
            descrescente.append(jtem)

def criar_txt(arquivo):
    txt = open('lista de arquivos.txt', 'w')

    for item in arquivo:
        txt.write("Arquivo: " + str(item) + ", Espaco ocupado: " + str(os.stat(str(item)).st_size) + " bytes \n")            

criar_txt(descrescente)