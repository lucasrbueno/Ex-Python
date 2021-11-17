import psutil

print(psutil.pids())

pid = int(input("Qual PID você quer informações? "))
p = psutil.Process(pid)

print("Nome do Processo: ", p.name(), ", Uso de memória: ", p.memory_percent())
