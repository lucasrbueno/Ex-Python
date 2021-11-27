import os

def criar_txt(diretorio, arquivo):
    txt = open('lista de arquivos.txt', 'w')

    for item in arquivo:
        caminho = diretorio + str(item)
        txt.write(f"Arquivo: {i}, Espaco ocupado: {os.stat(caminho).st_size} bytes\n")

    txt.close()

# C:\\Users\\Lucas\\Desktop\\Exercicios-Python\\
diretorio = input("Qual diretório deseja obter os arquivos? ")
print(diretorio)

if os.path.exists(diretorio):
    arquivos = []
    tamanho = []

    lista_diretorio = os.listdir(diretorio)

    for item in lista_diretorio:
        caminho = diretorio + str(item)
        if os.path.isfile(caminho):
            arquivos.append(item)
            tamanho.append(os.stat(caminho).st_size)
    tamanho = sorted(tamanho, reverse=True)

    criar_txt(diretorio, arquivos)