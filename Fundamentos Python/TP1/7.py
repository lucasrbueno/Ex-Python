# 7. Escreva uma função chamada cumsum que receba uma lista de números e 
# retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é 
# a soma dos primeiros i+1 elementos da lista original. Por exemplo:
# t = [1, 2, 3,4, 5, 6]
# >>> cumsum(t)
# [1, 3, 6, 10, 15, 21]

t = [1, 2, 3, 4, 5, 6]

def cumsum(lista):
  lista_nova = []
  total = 0
  for i in lista:
    total += i
    lista_nova.append(total)
  return lista_nova

print(cumsum(t))