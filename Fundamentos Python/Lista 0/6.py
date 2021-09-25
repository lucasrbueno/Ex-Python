# O fatorial do Joãozinho : https://br.spoj.com/problems/FATORIAL/

import math

print(math.factorial(10))

numero = int(input("Digite um número: "))
resultado = 1
for i in range(1,numero+1):
  resultado *= i

resultadoString = str(resultado)
resultadoFinal = resultadoString.replace("0", "")
print(resultadoFinal[-1:])