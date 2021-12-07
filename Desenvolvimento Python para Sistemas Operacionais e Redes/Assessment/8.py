from random import randint
from collections import defaultdict
import time

N = 10000000
testes_de_tamanho = [2000000, 3000000, 5000000, 10000000]
testes_de_n_threads = [1, 2, 4]

# Apenas preenchendo a lista de forma simplificada:
lista = []
for i in range(N):
    lista.append(randint(1,10))

def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)

lista_primo_seq = lista.copy()
lista_primo_thread = lista.copy()

print(fatorial(5))

def calcula_tempo_seq(N):
  # Captura tempo inicial
  t_inicio = float(time.time())
  # Realiza o cálculo
  for i in range(N):
      lista_primo_seq[i] = fatorial(lista[i])
  # Captura tempo final
  t_fim = float(time.time())

  return t_fim - t_inicio

resultado = defaultdict(list)
for n_thread in testes_de_n_threads:
  for tamanho in testes_de_tamanho:
    print(n_thread, tamanho)
    if n_thread == 1:
      resultado[f"S{n_thread}"].append(calcula_tempo_seq(tamanho))
    # else:
    #   resultado[f"T{n_thread}"].append(calcula_tempo_thread(n_thread, tamanho))
    #   resultado[f"P{n_thread}"].append(calcula_tempo_processo(n_thread, tamanho, lista[:tamanho]))
      
print(resultado)
