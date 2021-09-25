# 16. Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios a cada vez que o usuário clicar na tela. 
# A ponta superior da estrela deve estar situada onde o usuário clicou. (código e printscreen)

import pygame

pygame.init()
largula_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largula_tela, altura_tela))


def desenho_estrela(BRANCO, x, y):
    pygame.draw.polygon(tela, BRANCO, [[x - 50, y], [x, y - 131], [x + 40, y],
                                           [x + 206, y - 7], [x + 42, y + 68],
                                           [x + 91, y + 195], [x - 15, y + 101],
                                           [x - 121, y + 187], [x - 72, y + 60],
                                           [x - 186, y - 5]], 0)

x = 400
y = 300

PRETO = (0, 0, 0)
BRANCO = (225, 225, 225)
tela.fill(PRETO)
terminou = False
while not terminou:
    desenho_estrela(BRANCO, x, y)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            desenho_estrela(BRANCO, x, y)
        if event.type == pygame.QUIT:
            terminou = True
    tela.fill(PRETO)

pygame.display.quit()
pygame.quit()