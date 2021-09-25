import pygame

from random import randrange 
from time import sleep

pygame.init()
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

tela.fill((randrange(255),randrange(255),randrange(255)))

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
LARANJA = (246, 130, 0)

a = 395
b = 300

terminou = False
while not terminou:

    pygame.draw.circle(tela, BRANCO, (a+5, b), 40)
    pygame.draw.circle(tela, BRANCO, (a+5, b+80), 55)
    pygame.draw.rect(tela, PRETO, (a, b-25, 5, 5), 0)

    pygame.draw.rect(tela, PRETO, (a-30, b-45, 70, 10), 0)
    pygame.draw.rect(tela, PRETO, (a-15, b-95, 40, 60), 0)
    pygame.draw.line(tela, PRETO, (a-95, b), (a-40, b+55), 8)
    pygame.draw.line(tela, PRETO, (a+45, b+50), (a+95, b+95), 8)
    pygame.draw.polygon(tela, LARANJA, [[a-5, b-5], [a-25, b+5], [a-5, b]], 0)

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
            tela.fill((randrange(255),randrange(255),randrange(255)))

pygame.display.quit()
pygame.quit()
