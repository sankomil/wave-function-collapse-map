import sys
import pygame

from classes import Grid, Draw, grid
from rules import *


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((WIDTH * SPRITE_SIZE * SCALE, HEIGHT * SPRITE_SIZE * SCALE))

    box = Grid()
    draw = Draw(box)

    draw.update()

    is_running = True
    finished = False

    while is_running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
        
        if not finished:
            result = box.wfc()
            print(result)
            if result == 0:
                finished = True
            
        draw.update()


        draw.draw(display)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
