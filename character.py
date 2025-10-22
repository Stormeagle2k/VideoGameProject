import pygame
from pygame.locals import *
import time

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
        self.speedx = 0
        self.speedy = 0
        self.momentum = 0

       
    def move(self, x):
        self.x = x

    def left(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.speedx -= 0.5
        if event.type == pygame.KEYUP:
                #for event in pygame.event.get():
            if self.speedx < 0:
                x = [1,2,3,4,5,6,7,8,9,10]
                for i in x:
                    self.speedx += 0.1
                    i += 1 
                    if self.speedx == 0:
                        break
                #self.speedx = 0


    def right(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.speedx += 0.5
            #for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if self.speedx > 0:
                y = [1,2,3,4,5,6,7,8,9,10]
                for i in y:
                    self.speedx -= 0.1
                    i += 1 
                    if self.speedx == 0:
                        break
                #self.speedx -= self.speedx

    def down(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            self.speedy += 0.5
        if event.type == pygame.KEYUP:
            if self.speedy > 0:
                y = [1,2,3,4,5,6,7,8,9,10]
                for i in y:
                    self.speedy -= 0.1
                    i += 1 
                    if self.speedx == 0:
                        break

    def up(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.speedy -= 0.5
        if event.type == pygame.KEYUP:
            if self.speedy < 0:
                y = [1,2,3,4,5,6,7,8,9,10]
                for i in y:
                    self.speedy += 0.1
                    i += 1 
                    if self.speedy == 0:
                        break

    def downleft(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
            self.speedy += 0.5
            self.speedx -= 0.5
        if event.type == pygame.KEYUP:
            if self.speedy > 0 and self.speedx < 0:
                x = [1,2,3,4,5,6,7,8,9,10]
                for i in x:
                    self.speedy -= 0.1
                    self.speedx += 0.1
                    i += 1
                    if self.speedy == 0 and self.speedx == 0:
                        break

    def downright(self,event):
        pass

    def upleft(self, event):
        pass           

    def upright(self, event):
        pass       



    def getspeedx(self):
        return self.speed[0]
    
    def getspeedy(self):
        return self.speed[1]

    def update(self, *args, **kwargs):
        self.rect.move_ip(self.speedx, self.speedy) # This is how it's moving
        return super().update(*args, **kwargs)
            

    def jump(self):
        pass

    def die(self):
        pass


