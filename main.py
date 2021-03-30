import pygame,sys,os
from square import Square
from individual import Individual
from genetic import Genetic
from food import Food
import matplotlib.pyplot

pygame.init()
pygame.font.init()

font = pygame.font.get_default_font()
font_info = pygame.font.SysFont(font,45)
font_guide = pygame.font.SysFont(font,22) 


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WINDOW_SIZE = (640,480)

POPULATION_SIZE = 10

FOOD_QUANT = 50

MUTATION_RATE = 0.05

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("GeneticCells")

genetic = Genetic(POPULATION_SIZE)
genetic.population_init(WINDOW_SIZE)

generations = []
sizes = []
vels = []
grades = []
quant_individuals = []

txt_info = 'gen: ' + str(genetic.generation)
txt_guide = 'Graphics keys: Sizes - s | Vel - v | Grades - g | Population - p'
render_info = font_info.render(txt_info,1,WHITE)
render_guide = font_guide.render(txt_guide,1,(200,200,200))

time = pygame.time.Clock()
fps = 60
ticks = 0

food_list = []

def food_init():
    for i in range(FOOD_QUANT):
        food_list.append(Food(WINDOW_SIZE))

def draw_food():
    for food in food_list:
        food.draw(window)

def draw_population():
    for individual in genetic.population:
        individual.square.draw(window)
        individual.square.update()

def food_collide():
    for individual in genetic.population:
        for food in food_list:
            if individual.square.rect.colliderect(food.rect):
                food_list.remove(food)
                individual.grade += 1

def graphs_data():
    avarage_size,avarage_vel,avarage_grade = genetic.avarage()
    sizes.append(avarage_size)
    vels.append(avarage_vel)
    grades.append(avarage_grade)
    quant_individuals.append(len(genetic.population))
    generations.append(genetic.generation)

def graph_show(x_list,y_list,title='',x_title='',y_title=''):
    matplotlib.pyplot.plot(x_list,y_list)
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.xlabel(x_title)
    matplotlib.pyplot.ylabel(y_title)
    matplotlib.pyplot.show()

food_init()

while True:

    ticks += 1
    window.fill((20,20,20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                graph_show(generations, sizes, 'Avarage sizes/generations', 'generations', 'Avarage sizes')

            if event.key == pygame.K_v:
                graph_show(generations, vels, 'Avarage velocity/generations', 'generations', 'Avarage velocity')

            if event.key == pygame.K_g:
                graph_show(generations, grades, 'Avarage grades/generations', 'generations', 'Avarage grade')

            if event.key == pygame.K_p:
                graph_show(generations, quant_individuals, 'Individuals/generations', 'generations', 'Individuals')
                
    draw_food()
    draw_population()
    food_collide()

    if ticks >= 180:
        ticks = 0
        
        graphs_data()

        genetic.solve(WINDOW_SIZE,MUTATION_RATE)

        food_init()

        txt_info = 'gen: ' + str(genetic.generation)
        render_info = font_info.render(txt_info,1,WHITE)

    
    window.blit(render_info,(10,10))
    window.blit(render_guide,(10,460))
    pygame.display.update()
    time.tick(fps)
