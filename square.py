import random
from main import WINDOW_SIZE
import pygame

pygame.init()

COLORS = [(200,200,0),(200,0,200),(0,200,200)]

class Square:
    def __init__(self,chromosome):

        self.init_pos = (random.randint(0,WINDOW_SIZE[0]), random.randint(0,WINDOW_SIZE[1]))
        self.rect = pygame.Rect(self.init_pos[0],self.init_pos[1],chromosome[0],chromosome[0])
        self.vel = chromosome[1]

        self.vel_x = self.vel
        self.vel_y = self.vel

        self.color = random.sample(COLORS)

    def draw(window):
        pygame.draw.rect(window,self.color,self.rect)
    
    def update():
        self.move

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x <= 0 or self.rect.x >= WINDOW_SIZE[0]:
            self.vel_x *= -1
        
        if self.rect.y <= 0 or self.rect.y >= WINDOW_SIZE[1]:
            self.vel_y *= -1
