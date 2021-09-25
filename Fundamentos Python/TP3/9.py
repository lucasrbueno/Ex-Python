# 9. Usando a biblioteca Pygame, escreva um programa que possui uma função que 
# desenha um círculo azul de 100 px de diâmetro no centro da tela.

import pygame
from time import sleep

pygame.init()

largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
tela.fill((0, 0, 0))

AZUL = (0, 0, 255)

terminou = False

while not terminou:
    pygame.draw.circle(tela, AZUL, (400, 300), 100)
    pygame.display.update()   
    sleep(0.4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

pygame.display.quit()
pygame.quit()