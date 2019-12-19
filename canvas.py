import numpy as np
from tile import Tile

class Canvas:

    def __init__(self, win, width, height, wide, high, strokes, depth, stroke_length):
        self.width = width
        self.height = height
        self.wide = wide
        self.high = high
        self.strokes = strokes
        self.depth = depth
        self.stroke_length = stroke_length
        self.tiles = []
        self.tile_width = width / wide
        self.tile_height = height / high

        for i in range(self.wide):
            self.tiles.append([])
            for j in range(self.high):
                self.tiles[i].append("")

        col = [[np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)], [np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)]]
        for i in range(wide - 1, -1, -1):
            for j in range(high-1, -1, -1):
                if not i == wide-1: col[0] = self.tiles[i+1][j].col
                if not j == high-1: col[1] = self.tiles[i][j+1].col
                self.tiles[i][j] =(Tile(win, i * self.tile_width, j * self.tile_height, self.tile_width, self.tile_height, col, depth))
                

    def draw(self):
        for i in self.tiles:
            for j in i:
                j.display()
