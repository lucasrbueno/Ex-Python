import psutil, time

interfaces = psutil.net_if_addrs()
nomes = []

for i in interfaces:
  nomes.append(str(i))
  
status = psutil.net_if_stats()

for i in nomes:
  print(i+":")
  for j in interfaces[i]:
    print("\t"+str(j))
  print("\t"+str(status[i]))
  print("-----------------------------------------------------------------------------------------------------------------------------------")


io_status = psutil.net_io_counters(pernic=True)
nomes = []
for i in io_status:
  nomes.append(str(i))
for j in nomes:
  print(j)
  print("\t"+str(io_status[j]))
for i in range(4):
  time.sleep(1)
  io_status = psutil.net_io_counters(pernic=True)
  for j in nomes:
    print(j)
    print("\t"+str(io_status[j]))