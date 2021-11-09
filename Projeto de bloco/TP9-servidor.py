import os
import subprocess
import platform
import nmap
import psutil
import cpuinfo
import time
import sched
import socket
import pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
disco = psutil.disk_usage('.')
info_cpu = cpuinfo.get_cpu_info()
scheduler = sched.scheduler(time.time, time.sleep)

def processos_rede():
    for i in psutil.pids():
        p = psutil.Process(i)
        conn = p.connections()
    if len(conn) > 0:
        if conn[0].status.ljust(13) != "ESTABLISHED  ":
            endl = conn[0].laddr.ip.ljust(11)
            portl = str(conn[0].laddr.port).ljust(5)
            endr = conn[0].laddr.ip.ljust(13)
            portr = str(conn[0].laddr.port).ljust(5)
        str(i).ljust(5)," End.  Tipo   Status        Endereço    Local   Porta L.        Endereço Remoto  Porta R."
        str("      ", obtem_nome_familia(conn[0].family)), " " + obtem_tipo_socket(conn[0].type), "   " + conn[0].status.ljust(13), endl , portl, "  " + endr, "  " + portr

def print_event(name):
    return 'EVENTO:', time.ctime(), name
    

def print_event2(name):
    return 'EVENTO:', time.ctime(), name, diretorio()

def execucao_evento():
    msg = ("----------------------------------------------------\n" 
    + 'INICIO: \n'
    + str(scheduler.enter(2, 1, print_event, ('primeira chamada',))) + "\n"
    + str(scheduler.enter(8, 1, print_event2, ('segunda chamada',))) + "\n"
    + '\nCHAMADAS ESCALONADAS DA FUNÇÃO:\n'
    + "----------------------------------------------------\n")
    return msg

def obtem_nome_familia(familia):
  if familia == socket.AF_INET:
      return("IPv4")
  elif familia == socket.AF_INET6:
      return("IPv6")
  elif familia == socket.AF_UNIX:
      return("Unix")
  else:
      return("-")

def obtem_tipo_socket(tipo):
  if tipo == socket.SOCK_STREAM:
    return("TCP")
  elif tipo == socket.SOCK_DGRAM:
    return("UDP")
  elif tipo == socket.SOCK_RAW:
    return("IP")
  else:
    return("-")

def interfaces():
    interfaces = psutil.net_if_addrs()
    io_status = psutil.net_io_counters(pernic=True)
    status = psutil.net_if_stats()

    nomes = []

    for i in interfaces:
        nomes.append(str(i))

    for i in nomes:
        print(i+":")
        for j in interfaces[i]:
            print("\t"+str(j))
        print("\t"+str(status[i]))
        print("-----------------------------------------------------------------------------------------------------------------------------------")

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

def diretorio():
    pasta_atual = os.listdir()

    lista_diretorios = []
    lista_arquivos = []

    for item in pasta_atual:
        if os.path.isfile(item):
            lista_arquivos.append(item)
        else:
            if item not in [".git", ".vscode"]:        
                lista_diretorios.append(item)

    msg = (lista_diretorios), (lista_arquivos)

    # print("LISTA DE DIRETÓRIOS:\n" + *lista_diretorios, sep=" \n")
    # print("\nLISTA DE ARQUIVOS:\n" + *lista_arquivos, sep=" \n")
    return msg

def mostra_informacoes():
    msg = ("Informações do computador: " "Frequência (MHz): " + str(round(psutil.cpu_freq().current, 2)) 
        + "\nNúcleos (físicos): " + str(psutil.cpu_count()) + " (" + str(psutil.cpu_count(logical=False)) + ")" 
        + "\nProcessador info: " + str(platform.processor()) + " | " + str(platform.node() + " | " + platform.platform() + " | " + platform.system()) 
        + "\nDisco info, Total: " + str(round(disco.total/(1024*1024*1024), 2)) + "GB ,     " 
        + "Usado: " + str(round(disco.used/(1024*1024*1024), 2)) + "GB ,       " 
        + "Livre: " + str(round(disco.free/(1024*1024*1024), 2)) + "GB" + ",       " 
        + "Percentual usado: " + str(disco.percent) + "%" 
        + "\nMemória total: " + str(round(psutil.virtual_memory().total/(1024*1024*1024), 2)) + "GB"
        + "\nUso da CPU: " + str(psutil.cpu_percent(interval=1, percpu=True))
        + "\nRede: " + str(psutil.net_if_addrs()['Ethernet0'][0].address))
    return msg

def processos():
    return [proc.info for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_percent'])]

host = socket.gethostname()
porta = 9999

socket_servidor.bind((host, porta))

socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    msg = socket_cliente.recv(15360000)

    if '$' == msg.decode('utf-8'): 
        print("Fechando conexao com", str(addr), "...")
        socket_cliente.close()
        break
    elif '1' in msg.decode('utf-8'): 
        msg = mostra_informacoes()
        print(msg)
        socket_cliente.send(msg.encode('utf-8'))
    elif '2' in msg.decode('utf-8'): 
        msg = str(processos())
        print(msg)
        socket_cliente.send(msg.encode('utf-8'))
    elif '3' in msg.decode('utf-8', 'ignore'): 
        msg = pickle.dumps(diretorio())
        socket_cliente.send(msg)
        print(msg)
    elif '4' in msg.decode('utf-8'): 
        msg = "zz"
        print(msg)
    else:
        msg = "O que quer dizer com isso? ---> " + msg.decode('utf-8') 
    

scheduler.run()    
socket_servidor.close()
input("Pressione qualquer tecla para sair...") 
