# 3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. 
# O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. 
# Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. 
# Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

fatorial = int(input("Entre um número: "))    

def calcularFatorial(fatorial):
    numero_inicial = 1    
    if fatorial < 0:    
        return "Não é possível utilizar números negativos"     
    else:    
        for i in range(1, fatorial + 1):    
            numero_inicial = numero_inicial * i    
    return f"O fatorial de {fatorial} é {numero_inicial}"

print(calcularFatorial(fatorial))


 