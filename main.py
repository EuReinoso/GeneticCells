import pygame,sys
from square import Square
from individual import Individual
from genetic import Genetic

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WINDOW_SIZE = (640,480)

POPULATION_SIZE = 150

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GeneticCells")

genetic = Genetic(POPULATION_SIZE)
genetic.population_init(WINDOW_SIZE)

time = pygame.time.Clock()
fps = 60

def draw_population():
    for individual in genetic.population:
        individual.square.draw(window)
        individual.square.update()

while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_population()

    pygame.display.update()
    time.tick(fps)
