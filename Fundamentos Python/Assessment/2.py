# 2. Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. 
# O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

soma = 0

n = int(input("Digite o valor desejado: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        soma = soma + i

print(soma)
    