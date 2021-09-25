import pygame
import psutil
import cpuinfo
import platform
import os
import time
import subprocess

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

def diretorio():
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

def notepad():
        for i in range(2, 1, -1):
                print ('%s %0.2f %0.2f' % (time.ctime(), time.time(), time.process_time()))
                print ('Dormindo', i, ' segs')
                pid = subprocess.Popen("notepad.exe").pid
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
          s = str(psutil.net_if_addrs()['Ethernet'][0].address)
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
diretorio()
notepad()

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

pygame.display.quit()