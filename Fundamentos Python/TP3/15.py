# 15. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 5 pontas no tamanho que preferir. (código e printscreen)

import pygame

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

DARK_BLUE  = (3, 5, 54)
STARRY     = ( 230, 255, 80 )

pygame.init()
window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
pygame.display.set_caption("Star")

centre_coord = ( WINDOW_WIDTH//2, WINDOW_HEIGHT//2 )
star_points  = [ (165, 151), (200, 20), (235, 151), (371, 144), (257, 219),
                 (306, 346), (200, 260), (94, 346), (143, 219), (29, 144)   ]

clock = pygame.time.Clock()
done = False
while not done:

    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True

    window.fill( DARK_BLUE )                             
    pygame.draw.polygon( window, STARRY, star_points )   
    pygame.display.flip()                                

    clock.tick_busy_loop(60)

pygame.quit()