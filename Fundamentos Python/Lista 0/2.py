# Faça um programa que peça um número inteiro e determine se ele é ou 
# não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("numero: "))
confirmar = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            confirmar = True
            break

if confirmar:
    print(num, "não é um número primo")
else:
    print(num, "é um número primo")
