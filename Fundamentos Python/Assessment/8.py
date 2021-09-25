import pygame
from random import randint

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0, 0, 0)
AMARELO = (225, 225, 0)
AZUL = (0, 0, 255)
BRANCO = (225, 225, 225)
tela.fill(PRETO)

class Circle:
    def __init__(self):
        self.rad = 50
        self.x_circulo = tela.get_width() / 2
        self.y_circulo = tela.get_height() - 525
        self.area = (self.x_circulo, self.y_circulo)
        self.cor = AZUL
        self.fonte = pygame.font.Font(None, 24)
        self.texto = self.fonte.render("Clique", 1, BRANCO)

    def desenhar_circulo(self, tela_def):
        return pygame.draw.circle(tela_def, self.cor, self.area, self.rad)

    def desenhar_texto(self):
        tela.blit(self.texto, (self.x_circulo - 25, self.y_circulo - 10))

class Rect(pygame.Rect):
    def __init__(self):
        self.altura = 50
        self.largura = 100
        self.x_retangulo = randint(0, largura_tela)
        self.y_retangulo = randint(0, altura_tela)
        self.area = pygame.Rect(self.x_retangulo, self.y_retangulo, self.largura, self.altura)
        self.cor = AMARELO

    def desenhar_retangulo(self, tela_def):
        pygame.draw.rect(tela_def, self.cor, self.area)

lista_de_retangulos = []

pygame.init()

terminou = False
while not terminou:
    tela.fill(PRETO)
    for r in lista_de_retangulos:
        r.desenhar_retangulo(tela)
    circulo = Circle()
    circulo.desenhar_circulo(tela)
    circulo.desenhar_texto()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if (circulo.x_circulo + circulo.rad >= x >= circulo.x_circulo - circulo.rad) and \
                    (circulo.y_circulo - circulo.rad <= y <= circulo.y_circulo + circulo.rad):
                retangulo = Rect()
                retangulo.desenhar_retangulo(tela)
                lista_de_retangulos.append(retangulo)
                for i, retangulo_2 in enumerate(lista_de_retangulos):
                    if retangulo_2 is not retangulo and pygame.Rect.colliderect(retangulo_2.area, retangulo.area):
                        lista_de_retangulos.pop(i)
                        if retangulo in lista_de_retangulos:
                            lista_de_retangulos.pop(-1)
        if event.type == pygame.QUIT:
            terminou = True
        pygame.display.update()

pygame.display.quit()
pygame.quit()