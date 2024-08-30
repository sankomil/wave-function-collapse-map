import pygame
import os

from classes.grid import Grid
from rules import *

class Draw:

    def __init__(self, box) -> None:
        self.grid_box = box
        self.window = pygame.Surface((WIDTH * SPRITE_SIZE * SCALE, HEIGHT * SPRITE_SIZE * SCALE))
        self.text = pygame.font.Font(pygame.font.get_default_font(), 14)
    

    def update(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                entropy = self.grid_box.grid[x][y].entropy
                print(self.grid_box.grid[x][y].pos)
                sprite = self.grid_box.grid[x][y].pos[0]
                tile = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
                
                
                if entropy <= 0:
                    tile = pygame.image.load(os.path.join(tile_loc[sprite])).convert_alpha()
                tile = pygame.transform.scale_by(tile, (SCALE, SCALE))
                self.window.blit(tile, (x * SPRITE_SIZE * SCALE, y * SPRITE_SIZE * SCALE))
    
    def draw(self, display):
        display.blit(self.window, (0, 0))

    
