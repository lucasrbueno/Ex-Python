import time
import subprocess, psutil, time

for i in range(8, 1, -1):
  print ('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.process_time()))
  print ('Dormindo', i, ' segs')
  # Apenas cria um processo (calculadora) para testar
  pid = subprocess.Popen("notepad.exe").pid
  time.sleep(i)
