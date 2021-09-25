# 7. Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), 
# toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

import pygame
from random import randint

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

PRETO = (0, 0, 0)
AMARELO = (225, 225, 0)
BRANCO = (225, 225, 225)
tela.fill(PRETO)

def desenhar_retangulo(x, y, amarelo, comprimento, altura): 
    pygame.draw.rect(tela, amarelo, pygame.Rect(x, y, comprimento, altura))

pygame.init()

terminou = False
while not terminou:
    x = randint(0, largura_tela)
    y = randint(0, altura_tela)
    comprimento = 100
    altura = 50
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            desenhar_retangulo(x, y, AMARELO, comprimento, altura)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                desenhar_retangulo(x, y, AMARELO, comprimento, altura)
        pygame.display.update()
        if event.type == pygame.QUIT:
            terminou = True
        pygame.display.update()

pygame.display.quit()
pygame.quit()