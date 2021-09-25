# 11. Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. 
# Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de 
# face 6 do dado dentre esses 50 lançamentos. 

import random

numero_6 = 0
vetor = []

for i in range(51):
    dado = random.randint(1,6)
    vetor.append(dado)
    if dado == 6:
        numero_6 += 1

print((numero_6/50) * 100,"%")
print("Vetor total:", vetor)
