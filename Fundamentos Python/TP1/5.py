# 5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:
# Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
# Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
# Dada uma tupla e um elemento, elimine esse elemento da tupla.
# Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

tupla = (1, 2, 3, 4)
num = 3

def numeroExiste(tupla, num):
    if num in tupla:
        return f"Sim, o número {num} existe na tupla."
    else:
       return f"Não existe o número {num}"

print(numeroExiste(tupla, num))

def numeroMetade(tupla):
    metade_1 = tupla[:len(tupla)//2]
    metade_2 = tupla[len(tupla)//2:]
 
    total = metade_1,  metade_2
    return total

print(numeroMetade(tupla))

def numeroDeleta(tupla, num):
    a_generator = (number for number in tupla if number != num)

    return tuple(a_generator)

print(numeroDeleta(tupla, num))

def numeroInvertido(tupla):
    return tupla[::-1] 

print(numeroInvertido(tupla))