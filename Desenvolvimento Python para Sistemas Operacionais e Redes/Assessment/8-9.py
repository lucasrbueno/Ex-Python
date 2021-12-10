from random import randint
from collections import defaultdict
import time
import multiprocessing
import threading

N = 10000000

testes_de_tamanho = [2000000, 3000000, 5000000, 10000000]
testes_de_n_threads = [1, 2, 4]

def fatorial(n):
  fat = n
  for i in range(n-1, 1, -1):
      fat = fat * i
  return(fat)

def calcula_tempo_seq(N):
  vetorA = []
  vetorB = []

  inicio = time.time()

  for i in range(N):
    vetorA.append(randint(1,10))

  for i in vetorA:
    vetorB.append(fatorial(i))

  fim = time.time()
  print("Tempo de execução sequencial:", round(fim - inicio, 2))

def calcula_tempo_processo(N):
  inicio = time.time()

  vetorA = []
  vetorB = []
  multi = 4

  for i in range(N):
    vetorA.append(randint(1,10))

  for i in vetorA:
    vetorB.append(fatorial(i))

  começo = multiprocessing.Queue()
  termino = multiprocessing.Queue()

  list_proc = []
  for i in range(multi):
      inicial = i * int(N / multi)
      finalidade = (i + 1) * int(N / multi)
      começo.put(vetorA[inicial:finalidade])
      m = multiprocessing.Process(target=fatorial, args=(começo, termino))
      m.start()
      list_proc.append(m)

  for m in list_proc:
      m.join()
  
  fim = time.time()

  print("Tempo total multiprocessing:", (fim - inicio), 2)
 

def calcula_tempo_threading(N):
  inicio = time.time()

  vetorA = []
  vetorB = []
  lista_threads = []
  nthreads = 4

  for i in range(N):
    vetorA.append(randint(1,10))

  for i in vetorA:
    vetorB.append(fatorial(i))

  for i in range(nthreads):
        inicial = i * int(N/nthreads)
        finalidade = (i + 1) * int(N/nthreads)
        t = threading(target=fatorial, args=(N, inicial, finalidade))
        t.start()
        lista_threads.append(t)
        for t in lista_threads:
            t.join()

  fim = time.time()

  print("Tempo total threading:", (fim - inicio), 2)

calcula_tempo_seq(N)
calcula_tempo_threading(N)
calcula_tempo_processo(N)

resultado = defaultdict(list)
for n_thread in testes_de_n_threads:
  for tamanho in testes_de_tamanho:
    print(n_thread, tamanho)
    if n_thread == 4:
      resultado[f"S{n_thread}"].append(calcula_tempo_seq(tamanho))
    else:
      resultado[f"T{n_thread}"].append(calcula_tempo_threading(n_thread, tamanho))
      resultado[f"P{n_thread}"].append(calcula_tempo_processo(n_thread, tamanho))