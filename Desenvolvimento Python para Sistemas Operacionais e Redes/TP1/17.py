import psutil, time

for i in range(20):
    time.sleep(1)
    print(psutil.cpu_times(percpu=True))