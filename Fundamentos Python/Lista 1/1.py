# Dado uma tupla de tuplas, calcular a soma de cada uma das tuplas e por fim calcular a média total das tuplas.

tuplas = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))
total = 0
for index, tupla in enumerate(tuplas):
  soma = sum(tupla)
  total += soma
  print(f"{index} : {soma}")
print(f"Média total : {total/len(tuplas)}")