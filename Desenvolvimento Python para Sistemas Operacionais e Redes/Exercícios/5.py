import os
from datetime import datetime

inicio = datetime.now()

def busca_arquivo(diretorio, arquivo):
    pasta_atual = os.listdir(diretorio)
    for item in pasta_atual:
        path_item = os.path.join(diretorio, item)  
        if os.path.isfile(path_item):
            if item == arquivo:
                return True
    return False
print(busca_arquivo("/Users/Lucas/Desktop/Exercicios-Python", "aaaaa.txt"))


fim = datetime.now()
print(fim - inicio)
