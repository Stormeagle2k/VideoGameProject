import pygame
from pygame.locals import *

class HopCube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,0,255))