import pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file = 'PixelCaveArt2.png', location=(0,0)):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('PixelCaveArt2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

bground = pygame.image.load('PixelCaveArt2.png')