import pygame
from pygame.locals import *
import sys
 
pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption(title='Square Hop')

bground = pygame.image.load('PixelCaveArt2.png')

FPS = pygame.time.Clock()
FPS.tick(30)

# This keeps the game open. Press backspace to close.
run = True
while run:
    window.blit(bground, (0,0))
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False

    
    pygame.display.update()

