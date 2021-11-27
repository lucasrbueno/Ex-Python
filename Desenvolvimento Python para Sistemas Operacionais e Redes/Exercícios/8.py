from threading import Thread
import time
from random import randint

def calcula_percent(lista, inicio, fim):
    # Realiza o cálculo
    for i in range(inicio, fim):
        lista[i] = lista[i] * 0.1

N = 1000000        
numero_threads = 2

# Apenas preenchendo a lista de forma simplificada:
lista = []
for i in range(N):
    lista.append(randint(1,1000))

# Captura tempo inicial
t_inicio = float(time.time())

lista_de_threads = []

for i in range(numero_threads):
  inicio = i * N//numero_threads
  fim = (i+1) * N//numero_threads
  t0 = Thread(target=calcula_percent, args=(lista, inicio, fim))
  t0.start() # inicia thread 0
  lista_de_threads.append(t0)


for t in lista_de_threads:
    t.join()

# Captura tempo final
t_fim = float(time.time())

print(f"Tempo total {numero_threads} threads em segundos:", t_fim - t_inicio)