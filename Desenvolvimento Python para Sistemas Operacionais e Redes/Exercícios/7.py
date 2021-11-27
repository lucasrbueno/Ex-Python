from threading import Thread
from time import sleep

def dizer_oi(i):
    for contador in range(10):
        print (f"Olá mundo{contador}! Da thread:", i)
        sleep(0.1)

lista_de_threads = []
for index in range(5):
    t = Thread(target=dizer_oi, args=(index,))
    t.start() # inicia thread 0
    lista_de_threads.append(t)

for t in lista_de_threads:
    t.join()

print("acabou a execução de todas as threads")
