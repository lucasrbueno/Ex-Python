# 3. Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e 
# calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. 
# Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def potencia(a, b):
    i = 0
    multiplicacao = 1
    while i < b:
        multiplicacao *= a
        i += 1
    print(multiplicacao)

def potencia_simples(a, b):
    print(a ** b)

a = int(input("Insira o número: "))
b = int(input("Insira a potência: "))

potencia(a, b)
potencia_simples(a, b)
