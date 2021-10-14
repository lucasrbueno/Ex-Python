import time, psutil

for i in psutil.net_connections():
  print(i)

a = psutil.net_io_counters().bytes_sent
b = psutil.net_io_counters().bytes_recv
c = psutil.net_io_counters().packets_sent
d = psutil.net_io_counters().packets_recv

time.sleep(1)

vazao_s = psutil.net_io_counters().bytes_sent - a
vazao_r = psutil.net_io_counters().bytes_recv - b

a = a /1024/1024/1024
b = b /1024/1024/1024

print("Gbytes enviados",a)
print("Gbytes Recebidos",b)
print("Pacotes enviados",c)
print("Pacotes recebidos",d)
print("")
print("Vazão bytes enviados",vazao_s)
print("Vazão bytes recebidos",vazao_r)
