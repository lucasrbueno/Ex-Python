# 4. Escreva um programa em Python que leia uma lista de 5 números inteiros e a apresente na ordem inversa. Imprima a lista  no final. 
# Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].

vetor = []

for i in range(0, 5):
    escolha_usuario = int(input("Escolha o número para inserir no vetor: "))
    vetor.append(escolha_usuario)

print(vetor[::-1])