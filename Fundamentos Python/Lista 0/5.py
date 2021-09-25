# Faça um programa que leia uma quantidade indeterminada de números positivos 
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
# A entrada de dados deverá terminar quando for lido um número negativo.

numero = int(input("Digite um número: "))
lista_um, lista_dois, lista_tres, lista_quatro = [], [], [], []

while(numero >= 0):
  if (0 <= numero < 26):
      lista_um.append(numero)
  elif (26 <= numero < 51):
      lista_dois.append(numero)
  elif (51 <= numero < 76):
      lista_tres.append(numero)
  elif (76 <= numero < 101):
      lista_quatro.append(numero)  
  numero = int(input("Digite um novo número: "))

print(f"Lista um: {lista_um}")
print(f"Lista dois: {lista_dois}")
print(f"Lista três: {lista_tres}")
print(f"Lista quatro: {lista_quatro}")