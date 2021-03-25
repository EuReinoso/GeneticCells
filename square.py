import random
import pygame

pygame.init()

COLORS = [(200,200,0),(200,0,200),(0,200,200)]

class Square:
    def __init__(self,chromosome,window_size):
        self.window_size = window_size
        self.init_pos = (random.randint(0,self.window_size[0]), random.randint(0,self.window_size[1]))
        self.rect = pygame.Rect(self.init_pos[0],self.init_pos[1],chromosome[0],chromosome[0])
        self.vel = chromosome[1]
        self.vel_x = 0
        self.vel_y = 0

        if random.random() < 0.5:
            self.vel_x = self.vel
        else:
            self.vel_x =-self.vel_x

        if random.random() < 0.5:
            self.vel_y = self.vel
        else:
            self.vel_y = -self.vel

        self.color = COLORS[random.randrange(0,len(COLORS))]

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)
    
    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x <= 0 or self.rect.x >= self.window_size[0]:
            self.vel_x *= -1
        
        if self.rect.y <= 0 or self.rect.y >= self.window_size[1]:
            self.vel_y *= -1
