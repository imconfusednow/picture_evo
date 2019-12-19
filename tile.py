import pygame
import numpy as np

class Tile:

    def __init__(self, win, x, y, width, height, col, diff):
        self.win = win
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.col = [ np.random.randint(-diff,diff + 1),  np.random.randint(-diff,diff + 1),  np.random.randint(-diff,diff + 1)]
        for i in range(3):
            self.col[i] = round((col[0][i] + col[1][i] ) / 2) + self.col[i]
            self.col[i] = 255 if self.col[i] > 255 else self.col[i]
            self.col[i] = 0 if self.col[i] < 0 else self.col[i]


    def display(self):
        pygame.draw.rect(self.win, self.col,
                           ((self.x), (self.y), self.width, self.height))
