import os
from datetime import datetime
import time

inicio = datetime.now()

pasta_atual = os.listdir()

lista_diretorios = []
lista_arquivos = []
lista_arquivos_internos = {}

for item in pasta_atual:
    if os.path.isfile(item):
        lista_arquivos.append(item)
    else:
        if item not in [".git", ".vscode"]:        
            lista_diretorios.append(item)
            lista_arquivos_internos[item] = os.listdir(item)
print("LISTA DE DIRETÓRIOS")
print(*lista_diretorios, sep=" \n")
print("LISTA DE ARQUIVOS")
print(*lista_arquivos, sep=" \n")
print("LISTA DE ARQUIVOS INTERNOS")
for chave, valor in lista_arquivos_internos.items():
    print(chave, valor)

fim = datetime.now()
print(fim - inicio)
