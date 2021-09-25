# 10. Faça um programa que leia um vetor vet de 20 posições. 
# O programa deve gerar, a partir do vetor lido, um outro vetor pos que contenha apenas os valores inteiros positivos de vet. 
# A partir do vetor pos, deve ser gerado um outro vetor semdup que contenha apenas uma ocorrência de cada valor de pos.

vetor = [10, 20, 20, -10, 30, 10, 20, -20, 10, 30, 10, -20, 20, 10, 30, -10, 20, 20, 10, -30]
pos = []
semdup = []

for i in vetor:
    if i < 0:
        pos.append(i)
semdup = set(pos)

print(pos)
print(semdup)