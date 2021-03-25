import random
from main import WINDOW_SIZE
import pygame

pygame.init()

class Square:
    def __init__(self,chromosome):

        self.init_pos = (random.randint(0,WINDOW_SIZE[0]), random.randint(0,WINDOW_SIZE[1]))
        self.rect = pygame.Rect(self.init_pos[0],self.init_pos[1],chromosome[0],chromosome[0])
        self.vel = chromosome[1]
        

