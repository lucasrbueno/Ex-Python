import os

pasta_atual = os.listdir()

lista_arquivos = []

for item in pasta_atual:
    if os.path.isfile(item):
        lista_arquivos.append(item)

print("LISTA DE ARQUIVOS")
print(*lista_arquivos, sep=" \n")
