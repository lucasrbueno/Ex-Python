# 4. Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. 
# Use as mesmas especificações do item anterior.

fatorial = int(input("Entre um número: "))    

def calcularFatorial(fatorial):
    num = 1
    
    while fatorial >= 1:
        num = num * fatorial
        fatorial = fatorial - 1
    return num

print(calcularFatorial(fatorial))