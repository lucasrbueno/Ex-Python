import pygame, psutil

LARGURA_TELA = 800
ALTURA_TELA = 600
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 32)

s1 = pygame.surface.Surface((LARGURA_TELA, ALTURA_TELA/3))
s2 = pygame.surface.Surface((LARGURA_TELA, ALTURA_TELA/3))
s3 = pygame.surface.Surface((LARGURA_TELA, ALTURA_TELA/3))

def mostrar_uso_memoria():
    mem = psutil.virtual_memory()
    larg = LARGURA_TELA - (2 * 20)
    tela.fill(PRETO)
    pygame.draw.rect(s1, AZUL, (20, 50, LARGURA_TELA-2*20, 70))
    tela.blit(s1, (0, 0))
    larg = larg * mem.percent / 100
    pygame.draw.rect(tela, VERMELHO, (20, 50, larg, 70))
    total = round(mem.total / pow(2, 30), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, BRANCO)
    tela.blit(text, (20, 10))

def mostrar_uso_cpu():    
    capacidade = psutil.cpu_percent(interval=0)
    larg = LARGURA_TELA - (2 * 20)
    pygame.draw.rect(s2, AZUL, (20, 50, LARGURA_TELA-2*20, 70))
    tela.blit(s2, (0, ALTURA_TELA/3))
    larg = int((larg * capacidade) / 100)
    pygame.draw.rect(tela, VERMELHO, (20, 250, larg, 70))
    text = font.render("Uso de CPU:", 1, BRANCO)
    tela.blit(text, (20, 210))

def mostrar_uso_disco():    
    disco = psutil.disk_usage(".")
    larg = LARGURA_TELA - (2 * 20)
    pygame.draw.rect(s3, AZUL, (20, 50, LARGURA_TELA-2*20, 70))
    tela.blit(s3, (0, 2*ALTURA_TELA/3))
    larg = int((larg * disco.percent) / 100)
    pygame.draw.rect(tela, VERMELHO, (20, 450, larg, 70))
    total = round(disco.total / pow(2, 30), 2)
    text_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(text_barra, 1, BRANCO)
    tela.blit(text, (20, 410))

def rede():
    dic_interfaces = psutil.net_if_addrs()
    text_barra = "Endereço Ethernet: " + str(dic_interfaces['Ethernet'][0].address)
    text = font.render(text_barra, 1, BRANCO)
    tela.blit(text, (20, 550))

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.init()
clock = pygame.time.Clock()

cont = 60
terminou = False
while (not terminou):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            terminou = True
    if (cont == 60):
        mostrar_uso_memoria()
        mostrar_uso_cpu()
        mostrar_uso_disco()
        rede()
        cont = 0
    pygame.display.update()
    clock.tick(60)
    cont += 1 
pygame.display.quit()