import os, time

lista = os.listdir()
arquivos = {}

for item in lista:
    if os.path.isfile(item):
        caminho = os.path.splitext(item)[1]
        if not caminho in arquivos:
            arquivos[caminho] = []
        arquivos[caminho].append(item)

for item in arquivos:
    for j in arquivos[item]:
        tempo = os.stat(j)
        print(f"Nome do arquivo:  {j}, tempo de criação: {time.ctime(tempo.st_mtime)}")