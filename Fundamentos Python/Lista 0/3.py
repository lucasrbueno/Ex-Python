# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números 
# primos existentes entre 1 e um número inteiro informado pelo usuário.

numero = int(input("Digite um número: "))

def is_prime(numero):
      divisores = []
      for i in range(2,numero):
        if numero % i == 0:
            divisores.append(i)
        if len(divisores) == 0:
            return True
        else:
            return False
is_prime(numero)

lista_primos = []
for i in range(2, numero):
  if is_prime(i):
    lista_primos.append(i)
print(lista_primos)

