from tile import Tile
from canvas import Canvas
import pygame
import numpy as np

pygame.init()

this_canvases = []
saved_canvases = []
width = 1500
height = 1000
nwtiles = 300
nhtiles = 200

win = pygame.display.set_mode((width, height))

def setup(wide, high): 
    global this_canvases
    global saved_canvases

    
    for t in range(2):
        this_canvases.append(Canvas(win, width, height, wide, high, 1, 5, 10))
        
    for t in range(2):
        this_canvases[t].draw()


def draw(num):
    this_canvases[num].draw()

def combine(num):
    global this_canvases
    global saved_canvases

    if len(saved_canvases) < 4:
        saved_canvases.append(this_canvases[num])
        this_canvases = []
        setup(nwtiles, nhtiles)
        return

    this_canvases = []

    for t in range(2):
        this_canvases.append(Canvas(win, width, height, nwtiles, nwtiles, 1, 5, 10))

    saved_canvases = []


loop = True


win.fill((255, 255, 255))
setup(nwtiles, nhtiles)

num = 1


while loop:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                num = 0 if num == 1 else 1
                draw(num)
            if event.key == pygame.K_RETURN:
                combine(num)
                draw(num)




