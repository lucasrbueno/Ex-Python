import os, time

list = os.listdir()
arquivos = {}

for i in list:
    if os.path.isfile(i):
        caminho = os.path.splitext(i)[1]
        if not caminho in arquivos:
            arquivos[caminho] = []
        arquivos[caminho].append(i)

for i in arquivos:
    for j in arquivos[i]:
        status = os.stat(j)
        print(f"Nome do arquivo:  {j}, tempo de criação: {time.ctime(status.st_mtime)}")