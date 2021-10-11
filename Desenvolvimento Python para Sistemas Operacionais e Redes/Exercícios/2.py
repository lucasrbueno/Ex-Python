import psutil, time, subprocess

psutil.cpu_percent(percpu=True)
for i in range(3):
    time.sleep(0.1)
    print(psutil.cpu_percent(percpu=True))

print(subprocess.run("calc"))
print(subprocess.run(["notepad", "arq_texto.txt"]))
# subprocess.Popen()