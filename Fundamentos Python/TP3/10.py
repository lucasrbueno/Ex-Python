# 10. Usando a biblioteca Pygame, escreva um programa que possui uma 
# função que desenha um quadrado vermelho de 100 px de lado no centro da tela. 
# O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador. 
# Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado.

import pygame
from time import sleep

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

tela.fill((0, 0, 0))

VERMELHO = (255, 0, 0)

a = 350
b = 250

terminou = False
while not terminou:

    pygame.draw.rect(tela, VERMELHO, (a, b, 100, 100), 0)
    pygame.display.update()  
    sleep(0.4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                a -= 5
            if event.key == ord('d'):
                a += 5
            if event.key == ord('w'):
                b -= 5
            if event.key == ord('s'):
                b += 5
            tela.fill((0, 0, 0))

pygame.display.quit()
pygame.quit()
