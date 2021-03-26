from random import randint
import pygame

pygame.init()

COLOR = (200,0,0)

class Food:
    def __init__(self,window_size):
        self.window_size = window_size
        self.size = 10
        self.color = COLOR
        self.rect = pygame.Rect(randint(0,window_size[0] - self.size),
                                randint(0,window_size[1]- self.size)
                                ,self.size,self.size)
    
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect,0,10)
    