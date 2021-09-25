# 14. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro da tela. 
# Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada. (código e printscreen)

import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))

def quadrado(VERMELHO, x, y):
    pygame.draw.rect(tela, VERMELHO, pygame.Rect(x - 50, y - 50, 50, 50))

PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
VERMELHO = (225, 0, 0)

x = 400
y = 300

tela.fill(PRETO)
terminou = False
while not terminou:
    quadrado(VERMELHO, x, y)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            quadrado(VERMELHO, x, y)
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()