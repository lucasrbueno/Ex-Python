# 6. Escreva um programa em Python que receba três valores reais X, Y e Z, 
# guarde esses valores numa tupla e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, 
# neste caso, retorne qual o tipo de triângulo formado.
# Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: 
# o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados.
# Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

# Triângulo Equilátero: os comprimentos dos três lados são iguais.
# Triângulo Isósceles: os comprimentos de dois lados são iguais.
# Triângulo Escaleno: os comprimentos dos três lados são diferentes.

x = 5
y = 2
z = 4

tupla = (x, y, z)

def triangulo(tupla):
    if tupla[0] == tupla[1] and tupla[1] == tupla[2] and tupla[0] == tupla[2]:
        return "O triângulo é equilátero."
    elif tupla[0] == tupla[1] or tupla[1] == tupla[2] or tupla[0] == tupla[2]:
        return "O triângulo é isósceles."
    else:
        return "O triângulo é escaleno."

print(triangulo(tupla))