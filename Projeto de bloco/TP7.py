import os
import subprocess
import platform
import nmap
import pygame
import psutil
import cpuinfo
import time
import sched
import socket

interfaces = psutil.net_if_addrs()
io_status = psutil.net_io_counters(pernic=True)
status = psutil.net_if_stats()

def obter_hostnames(host_validos):
  nm = nmap.PortScanner()
  for i in host_validos:
      try:
          nm.scan(i)
          print("O IP possui o nome", nm[i].hostname())
          print(nm[i].hostname())
          for proto in nm[i].all_protocols():
              print("-----------------------------------------------------")
              print('Protocolo : %s' % proto)

              lport = nm[i][proto].keys()
              for port in lport:
                  print ('Porta: %s\t Estado: %s' % (port, nm[i][proto][port]['state']))          
      except:
          print("O IP deu problema")
          pass

def retorna_codigo_ping(hostname):
  """Usa o utilitario ping do sistema operacional para encontrar o host. ('-c 5') indica, em sistemas linux, que deve mandar 5 pacotes. ('-W 3') indica, em sistemas linux, que deve esperar 3 milisegundos por uma resposta. Esta funcao retorna o codigo de resposta do ping """

  plataforma = platform.system()
  args = []

  if plataforma == "Windows":
      args = ["ping", "-n", "1", "-l", "1", "-w", "100", hostname]
  else:
      args = ['ping', '-c', '1', '-W', '1', hostname]
    
  ret_cod = subprocess.call(args, stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
  return ret_cod

def verifica_hosts(base_ip):
  """Verifica todos os host com a base_ip entre 1 e 255 retorna uma lista com todos os host que tiveram resposta 0 (ativo)"""
  print("Mapeando\r")
  host_validos = []
  return_codes = dict()

  for i in range(1, 255):
      return_codes[base_ip + '{0}'.format(i)] = retorna_codigo_ping(base_ip + '{0}'.format(i))
      if i %20 ==0:
          print(".", end = "")
      if return_codes[base_ip + '{0}'.format(i)] == 0:
          host_validos.append(base_ip + '{0}'.format(i))
  print("\nMapping ready...")

  return host_validos

def execucao_ip():
  ip_string = input("Entre com o ip alvo: ")
  ip_lista = ip_string.split('.')
  base_ip = ".".join(ip_lista[0:3]) + '.'
  print("O teste será feito na sub rede: ", base_ip)
  host_validos = verifica_hosts(base_ip)
  print ("Os host válidos são: ", host_validos)
  print("-----------------------------------------------------")
  print("Iniciando nmap.PortScanner")
  obter_hostnames(host_validos)
  print("-----------------------------------------------------")
  print("Fim")

scheduler = sched.scheduler(time.time, time.sleep)

disco = psutil.disk_usage('.')

def mostra_info_cpu():
  s1.fill(branco)
  mostra_texto(s1, "Nome:", "brand_raw", 10)
  mostra_texto(s1, "Arquitetura:", "arch", 30)
  mostra_texto(s1, "Palavra (bits):", "bits", 50)
  mostra_texto(s1, "Frequência (MHz):", "freq", 70)
  mostra_texto(s1, "Núcleos (físicos):", "nucleos", 90)
  mostra_texto(s1, "Processador info:", "processador", 110)
  mostra_texto(s1, "Disco info:", "disco", 130)
  mostra_texto(s1, "Memória total: ", "memoria", 150)
  mostra_texto(s1, "Rede: ", "rede", 170)
  tela.blit(s1, (0, 0))

def arquivos():
  lista = os.listdir()
  dic = {}  
  for i in lista:  
          if os.path.isfile(i):
                  dic[i] = []
                  dic[i].append(os.stat(i).st_size) 
                  dic[i].append(os.stat(i).st_atime)  
                  dic[i].append(os.stat(i).st_mtime)  
  titulo = '{:11}'.format("Tamanho")  
  titulo = titulo + '{:27}'.format("Data de Modificação")
  titulo = titulo + '{:27}'.format("Data de Criação")
  titulo = titulo + "Nome"
  print(titulo)
  for i in dic:
          kb = dic[i][0] / 1000
          tamanho = '{:10}'.format(str('{:.2f}'.format(kb) + ' KB'))
          print(tamanho, time.ctime(dic[i][2]), " ", time.ctime(dic[i][1]), " ", i)

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
  print("LISTA DE DIRETÓRIOS")
  print(*lista_diretorios, sep=" \n")
  print("LISTA DE ARQUIVOS")
  print(*lista_arquivos, sep=" \n")

def mostra_info(pid):
  try:
    p = psutil.Process(pid)
    texto = '{:6}'.format(pid)
    texto = texto + '{:11}'.format(p.num_threads())
    texto = texto + " " + time.ctime(p.create_time()) + " "
    texto = texto + '{:8.2f}'.format(p.cpu_times().user)
    texto = texto + '{:8.2f}'.format(p.cpu_times().system)
    texto = texto + '{:10.2f}'.format(p.memory_percent()) + " MB"
    rss = p.memory_info().rss/1024/1024
    texto = texto + '{:10.2f}'.format(rss) + " MB"
    vms = p.memory_info().vms/1024/1024
    texto = texto + '{:10.2f}'.format(vms) + " MB"
    texto = texto + " " + p.exe()
    print(texto)
  except:
      pass

def notepad():
  for i in range(2, 1, -1):
    print ('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.process_time()))
    print ('Dormindo', i, ' segs')
    pid = subprocess.Popen("notepad.exe").pid
    print(mostra_info(pid))
    time.sleep(i)

def mostra_texto(s1, nome, chave, pos_y):
  text = font.render(nome, True, preto)
  s1.blit(text, (10, pos_y))
  if chave == "freq":
          s = str(round(psutil.cpu_freq().current, 2))
  elif chave == "nucleos":
          s = str(psutil.cpu_count())
          s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
  elif chave == "processador":
          s = str(platform.processor()) + " | " + str(platform.node() + " | " + platform.platform() + " | " + platform.system())
  elif chave == "disco":
          s = "Total: " + str(round(disco.total/(1024*1024*1024), 2)) + "GB ,     " + "Usado: " + str(round(disco.used/(1024*1024*1024), 2)) + "GB ,       " + "Livre: " + str(round(disco.free/(1024*1024*1024), 2)) + "GB" + ",       " + "Percentual usado: " + str(disco.percent) + "%"
  elif chave == "memoria":
          s = str(round(psutil.virtual_memory().total/(1024*1024*1024), 2)) + "GB"
  elif chave == "rede":
          s = str(psutil.net_if_addrs()['Ethernet0'][0].address)
  else:
          s = str(info_cpu[chave])

  text = font.render(s, True, cinza)
  s1.blit(text, (160, pos_y))
  
def mostra_uso_cpu(s, l_cpu_percent):
  s.fill(cinza)
  num_cpu = len(l_cpu_percent)
  x = y = 10
  desl = 10
  alt = s.get_height() - 2*y
  larg = (s.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
  d = x + desl
  for i in l_cpu_percent:
              pygame.draw.rect(s, vermelho, (d, y, larg, alt))
              pygame.draw.rect(s, azul, 	(d, y, larg, (1-i/100)*alt))
              d = d + larg + desl
  tela.blit(s, (0, altura_tela/2.5))  

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

def processos():
  for i in psutil.pids():
    p = psutil.Process(i)
    conn = p.connections()
    if len(conn) > 0:
        if conn[0].status.ljust(13) != "ESTABLISHED  ":
          endl = conn[0].laddr.ip.ljust(11)
          portl = str(conn[0].laddr.port).ljust(5)
          endr = conn[0].laddr.ip.ljust(13)
          portr = str(conn[0].laddr.port).ljust(5)
        print(str(i).ljust(5)," End.  Tipo   Status        Endereço    Local   Porta L.        Endereço Remoto  Porta R.")
        print("      ", obtem_nome_familia(conn[0].family), " " + obtem_tipo_socket(conn[0].type), "   " + conn[0].status.ljust(13), endl , portl, "  " + endr, "  " +portr)

info_cpu = cpuinfo.get_cpu_info()

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (100, 100, 100)
azul = (40, 40, 255)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 230, 0)

largura_tela = 1300
altura_tela = 700
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Informações de CPU")
pygame.display.init()

s1 = pygame.surface.Surface((largura_tela, altura_tela))

pygame.font.init()
font = pygame.font.Font(None, 24)
 
clock = pygame.time.Clock()
cont = 60

def print_event(name):
    print ('EVENTO:', time.ctime(), name)
    arquivos()

def print_event2(name):
    print ('EVENTO:', time.ctime(), name)
    notepad()

def execucao_evento():
    print("----------------------------------------------------")
    print ('INICIO:', time.ctime())
    scheduler.enter(2, 1, print_event, ('primeira chamada',))
    scheduler.enter(8, 1, print_event2, ('segunda chamada',))
    print ('CHAMADAS ESCALONADAS DA FUNÇÃO:', time.ctime())
    print("----------------------------------------------------")

execucao_evento()

execucao_ip()

diretorio()

processos()

terminou = False
while not terminou:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        terminou = True

  if cont == 60:

    mostra_info_cpu()
    mostra_uso_cpu(s1,psutil.cpu_percent(interval=1, percpu=True))

    cont = 0

    pygame.display.update()

    clock.tick(60)
    cont = cont + 1

scheduler.run()

pygame.display.quit()