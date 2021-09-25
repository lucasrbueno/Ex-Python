import pygame, random

# pygame.mixer.init()
pygame.font.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

quadrados_iniciais = 20

tempo_inicial = 10
terminou = False
preto = (0, 0, 0)
branco = (255, 255, 255)

class Quadradinho():
    def __init__(self):
        self.largura = 30
        self.altura = 30
        self.x = random.randint(0, largura_tela-self.largura)
        self.y = random.randint(20, altura_tela-self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
    def desenha(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

def mostra_tempo(tempo, pontos):
    font = pygame.font.Font(None, 24)
    text = font.render("Tempo: " + str(tempo) + "s | Pontuação: " + str(pontos), 1, branco)
    textpos = text.get_rect(centerx=tela.get_width()/2)
    tela.blit(text, textpos)

def mostra_pontuacao_final(tela, pontos):
    tela.fill(preto) 
    font = pygame.font.Font(None, 36)
    text = font.render("Pontuação: " + str(pontos) + " quadradinhos", 1, branco)
    textpos = text.get_rect(center=(tela.get_width()/2, tela.get_height()/2))
    tela.blit(text, textpos)

def pontuacao(pontos, quadradinho):
    r, g, b = quadradinho.cor[0], quadradinho.cor[1], quadradinho.cor[2]
    cor = "outra cor"
    ponto = 1 
    if r > 100 and r > g + b:
        ponto = 5
    if g > 100 and g > r + b:
        ponto = 10
    if b > 100 and b > r + g:
        ponto = 15
    print(r,g,b)

    return pontos + ponto
    
lista = []
for i in range(0, quadrados_iniciais):
    q = Quadradinho()
    q.desenha(tela)
    lista.append(q)

clock = pygame.time.Clock()

conta_clocks = 0

pontos = 0

conta_segundos = tempo_inicial

# efeito = pygame.mixer.Sound('C:/Users/admin/Desktop/Python/Fundamentos Python/Pygame/vinheta-xaropinho-rapaz-cut-mp3.mp3')

while not terminou:

    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
            pos = pygame.mouse.get_pos()

            for q in lista:
                if q.area.collidepoint(pos):
                    # efeito.play()
                    lista.remove(q)
                    
                    pontos = pontuacao(pontos, q)
                
        if event.type == pygame.QUIT:
            terminou = True
        
    conta_clocks = conta_clocks + 1

    if conta_clocks == 50:
        if conta_segundos >= 0:
            conta_segundos = conta_segundos - 1
        conta_clocks = 0   
        q = Quadradinho()
        lista.append(q)   	 

    if conta_segundos >= 0:  
        tela.fill(preto)
        for i in lista:
            i.desenha(tela) 
        mostra_tempo(conta_segundos, pontos)
    else:  
        mostra_pontuacao_final(tela, pontos)
        for q in lista:
            lista.remove(q)   	 

    pygame.display.update()

    clock.tick(50)

pygame.display.quit()