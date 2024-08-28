from collections import deque
import random

from heapq import heappush

from classes.sprite import Sprite
from rules import WIDTH, HEIGHT, NORTH, SOUTH, EAST, WEST


class Grid:

    def __init__(self, width=WIDTH, height=HEIGHT) -> None:
        self.width = width
        self.height = height
        self.grid = []
        self.entropy = []

        for x in range(width):
            row = []
            for y in range(height):
                sprite = Sprite(x, y)
                row.append(sprite)
                heappush(self.entropy, (sprite.entropy, sprite))
            self.grid.append(row)
        
        for x in range(width):
            for y in range(height):
                sprite = self.grid[x][y]
                if x > 0:
                    sprite.neighbours[EAST] = self.grid[x-1][y]
                if x < width - 1:
                    sprite.neighbours[WEST] = self.grid[x+1][y]
                if y > 0:
                    sprite.neighbours[NORTH] = self.grid[x][y-1]
                if y < height - 1:
                    sprite.neighbours[SOUTH] = self.grid[x][y+1]
        
    
    def get_lowest_entropy(self):
        if len(self.entropy) == 0:
            return 0
        index = 0
        while index < len(self.entropy) and self.entropy[index][0] == 0:
            index += 1
        return self.entropy[index][0]

    def get_lowest_entropy_list(self):
        if len(self.entropy) == 0:
            return []
        ent = self.get_lowest_entropy()
        index = 0
        result = []

        while index < len(self.entropy) and self.entropy[index][0] == ent:
            result.append(self.entropy[index][1])
            index += 1
        
        return result
    
    def wfc(self):
        lowest_entropy = self.get_lowest_entropy_list()

        if len(lowest_entropy) == 0:
            return 0
        
        sprite_collapse = random.choice(lowest_entropy)
        sprite_collapse.collapse()

        stack = deque()
        stack.append(sprite_collapse)

        while len(stack) > 0:
            sprite = stack.popleft()
            pos = sprite.pos
            directions = sprite.neighbours.keys()

            for d in directions:
                neighbour_sprite = sprite.neighbours[d]
                if neighbour_sprite.entropy != 0:
                    reduced = neighbour_sprite.reduce(d, pos)
                    if reduced:
                        stack.append(neighbour_sprite)
        
        self.entropy = []
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y].entropy != 0:
                    heappush(self.entropy, (self.grid[x][y].entropy, self.grid[x][y]))
    

