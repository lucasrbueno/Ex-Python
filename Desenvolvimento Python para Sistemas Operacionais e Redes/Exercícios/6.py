import psutil
import time

def compara_cpu_percent(x):
    return(x['cpu_percent'])

def ordenacao(processos):
    lista_ordenada = []
    for p in processos:
        try:
            pinfo = p.as_dict(attrs=['pid', 'name', 'cpu_percent'])
            p.cpu_percent()
            time.sleep(0.01)
            lista_ordenada.append({'pid': p.pid, 
                                    'nome': pinfo['name'], 
                                    'cpu_percent':p.cpu_percent()})
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            pass
    lista_ordenada.sort(key=compara_cpu_percent, reverse=True)
    return lista_ordenada

for i in ordenacao(psutil.process_iter()):
    print(i)