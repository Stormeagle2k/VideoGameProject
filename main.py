import pygame
from pygame.locals import *
import sys
from character import HopCube
from background import Background
from player import Player as pl
 
pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption(title='Square Hop')

FPS = pygame.time.Clock()
FPS.tick(30)


bground = Background('PixelCaveArt2.png', [0,0])

player = HopCube(0, 600)

window_rect = pygame.rect.Rect(0, 0, 785, 800)

# This keeps the game open. Press backspace to close.
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_BACKSPACE):
            run = False
            
    player.left(event)
    player.right(event)
    player.down(event)
    player.up(event)
    player.downleft(event)
    player.update()
    player.rect.clamp_ip(window_rect)
    # print(player.rect.x)

        
    
    window.fill([255, 255, 255])
    window.blit(bground.image, bground.rect)
    window.blit(player.surf, player.rect.center)
    
    pygame.display.flip()
    pygame.display.update()

