import psutil

for i in psutil.cpu_times(percpu=True):
    print(i)