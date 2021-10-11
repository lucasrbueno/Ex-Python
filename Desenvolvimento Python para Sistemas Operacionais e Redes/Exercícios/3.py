import matplotlib.pyplot as plt
import psutil, time

lista_cpu_percent = {"1" : [], "2" : []}

percpu = psutil.cpu_percent(percpu=True)
for i in range(20):
    percpu = psutil.cpu_percent(percpu=True)
    lista_cpu_percent["1"].append(percpu[0])
    lista_cpu_percent["2"].append(percpu[1])
    time.sleep(0.1)
print(lista_cpu_percent)

x = list(range(20))
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('CPU percent per nucleo')

ax1.plot(x, lista_cpu_percent["1"], 'o-')
ax1.set_ylabel('CPU 0')

ax2.plot(x, lista_cpu_percent["2"], '.-')
ax2.set_ylabel('CPU 1')

plt.show()
