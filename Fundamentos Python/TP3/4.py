# 4. Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. 
# Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)

t = [1, 2, 3, 4, 6, 8, 0, 10, 9]

zero = 0

for i in t:
    if i == 0:
        zero += 1

print(f"Existem um total de {zero} números iguais a 0")