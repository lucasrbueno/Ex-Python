# 1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. 
# O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

index = 0
n = int(input("numero: "))
soma = 0

while index <= n:
    index += 1

    if index % 2 != 0:
        soma += index

print(soma)
            