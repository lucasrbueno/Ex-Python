import psutil, time

input_pid_processo = int(input("Obter informações de PID específico: "))
processo = psutil.Process(input_pid_processo)

print(f"Nome do usuário: {processo.username}, tempo de criação: {time.ctime(processo.create_time())}, KBytes usados: {processo.memory_percent()}")
