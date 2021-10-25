import psutil, time

pid_processo = int(input("Obter informações de PID específico: "))

if psutil.pid_exists(pid_processo):
    processo = psutil.Process(pid_processo)
    print(f"Nome do usuário: {processo.username}, tempo de criação: {time.ctime(processo.create_time())}, KBytes usados: {processo.memory_percent()}")
