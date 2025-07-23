import pygame
from pygame.locals import *
import sys
from character import HopCube
from background import Background


class Game():
    def __init__(self):
        pass
 
pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption(title='Square Hop')

FPS = pygame.time.Clock()
FPS.tick(30)


bground = Background('PixelCaveArt2.png', [0,0])

player = HopCube()

# This keeps the game open. Press backspace to close.
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_BACKSPACE):
            run = False

    
    window.fill([255, 255, 255])
    window.blit(bground.image, bground.rect)
    window.blit(player.surf, [0,0], )
    
    pygame.display.flip()
    pygame.display.update()

