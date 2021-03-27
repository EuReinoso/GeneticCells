import random
import pygame

pygame.init()

COLORS = [(200,200,0),(200,0,200),(0,200,200),(100,100,0),(100,0,100),(0,100,100)]

class Square:
    def __init__(self,chromosome,window_size):
        self.window_size = window_size
        self.init_pos = (random.randint(1,self.window_size[0] - round(chromosome[0]) ), random.randint(1,self.window_size[1] - round(chromosome[0])))
        self.rect = pygame.Rect(self.init_pos[0],self.init_pos[1],chromosome[0],chromosome[0])
        self.vel = chromosome[1]
        self.vel_x = self.vel
        self.vel_y = self.vel

        if random.random() < 0.5:
            self.vel_x = - self.vel_x
        if random.random() < 0.5:
            self.vel_y = - self.vel_y

        self.color = COLORS[random.randrange(0,len(COLORS))]

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect,10,10)
    
    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.x < 0 or self.rect.x > self.window_size[0] - self.rect.width:
            self.vel_x = - self.vel_x
            
        if self.rect.y < 0 or self.rect.y > self.window_size[1] - self.rect.height:
            self.vel_y = - self.vel_y

    def change_rect(self,chromosome):
        self.rect.width = chromosome[0]
        self.rect.height = chromosome[0]

        self.vel_x = chromosome[1]
        self.vel_y = chromosome[1]
