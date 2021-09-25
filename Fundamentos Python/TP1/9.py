# 9. Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.

from collections import Counter

vetor = [10, 20, 20, 10, 30, 10, 10, 20, 20, 40]
print (len(Counter(vetor).keys()))