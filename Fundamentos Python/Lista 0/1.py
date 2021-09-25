# Faça um programa que peça 3 números inteiros, calcule e 
# mostre a quantidade de números pares e a quantidade de números impares.

index = 1
par = 0
impar = 0

while index <= 3:
    numero = int(input("numero: "))
    index += 1

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("par: ", par, "impar: ", impar)
            
 



