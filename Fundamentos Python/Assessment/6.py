# 6. Escreva uma função em Python que leia uma tupla contendo números inteiros, 
# retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.

tupla = (0, 1, 2, 3, 4, 5, 6, 7)
impar = []
posição_par = []

def lista_numero(tupla):
    for i in tupla:
        if i % 2 != 0:
            impar.append(i)   
        elif tupla.index(i) % 2 == 0: 
            posição_par.append(i)
    print(impar)
    print(posição_par)

lista_numero(tupla)

