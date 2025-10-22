from character import HopCube
import pygame
from pygame.locals import *

class Player(HopCube):
    def __init__(self):
        super().__init__()
        self.velocity = 1

    def left(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            HopCube.speedx = -1
            return HopCube.update(self)

