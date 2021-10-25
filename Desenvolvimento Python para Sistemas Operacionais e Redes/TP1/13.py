import subprocess

processo = subprocess.Popen("notepad")
print("PID: ", processo.pid)