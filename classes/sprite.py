import random
from rules import tile_neighbours

class Sprite:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.pos = list(tile_neighbours.keys())
        self.entropy = len(self.pos)
        self.neighbours = dict()
    

    def collapse(self):
        weights = [tile_neighbours[p]["TOTAL"] for p in self.pos]
        self.pos = random.choices(self.pos, weights=weights, k=1)
        self.entropy = 0
    
    def reduce(self, direction, neighbour_pos):
        reduced = False

        if self.entropy > 0:
            neigh = []
            for np in neighbour_pos:
                neigh = neigh + list(tile_neighbours[np][direction].keys())
            
            checked = []
            
            for p in self.pos.copy():
                for np in tile_neighbours[p][-direction].keys():
                    if np not in neigh and np not in checked and np in self.pos and len(self.pos) > 1:
                        self.pos.remove(np)
                        checked.append(np)
                        reduced = True
            
            self.entropy = len(self.pos)
        
        return reduced
    
    def __lt__(self, other):
        return self.entropy < other.entropy
    
    def __le__(self, other):
        return self.entropy <= other.entropy