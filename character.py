import pygame
from pygame.locals import *

class HopCube(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.surf = pygame.Surface((25,25))
        self.surf.fill((0,0,255))
        self.rect = pygame.rect.Rect((self.x, self.y, self.width, self.height))
        self.speed = [0,0]
        self.momentum = 0

       
    def move(self, x):
        self.x = x

    def getspeedx(self):
        return self.speed[0]
    
    def getspeedy(self):
        return self.speed[1]

    def update(self, *args, **kwargs):
        self.rect.move_ip(1, 0)
        return super().update(*args, **kwargs)
            

    def jump(self):
        pass

    def die(self):
        pass

    


