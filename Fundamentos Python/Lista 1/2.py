# Faça um programa que mostre os n termos da Série a seguir:
#  	S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

n = 30
lista1 = list(range(1,n))
lista2 = list(range(1,n*2))[::2]
termos = []
for i in range(0,n-1):
  termos.append(lista1[i]/lista2[i])
  print(f"{lista1[i]}/{lista2[i]}")

print(sum(termos))




