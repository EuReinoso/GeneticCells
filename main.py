import pygame,sys
from square import Square

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WINDOW_SIZE = (640,480)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GeneticCells")

chromosome = [10,3]
square = Square(chromosome,WINDOW_SIZE)

time = pygame.time.Clock()
fps = 60
while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    square.draw(window)
    square.update()

    pygame.display.update()
    time.tick(fps)
