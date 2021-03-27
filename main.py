import pygame,sys,os
from square import Square
from individual import Individual
from genetic import Genetic
from food import Food

pygame.init()

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

time = pygame.time.Clock()
fps = 60

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


food_init()

ticks = 0


while True:
    ticks += 1
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    draw_food()
    draw_population()

    food_collide()

    if ticks >= 180:
        ticks = 0

        genetic.population_order()
        genetic.best_individual(genetic.population[0])
        print(genetic.best_solution.chromosome,genetic.best_solution.grade, len(genetic.population))

        genetic.starve_kill()

        #new_population = []
        grade = genetic.population_assessment()

        for individual in range(0,len(genetic.population),1):

            father1 = genetic.father_select(grade)
            father2 = genetic.father_select(grade)

            #2sons
            # sons = genetic.population[father1].crossover(genetic.population[father2])
            # new_population.append(sons[0].mutation(MUTATION_RATE))
            # new_population.append(sons[1].mutation(MUTATION_RATE))

            #1son
            # sons = genetic.population[father1].crossover(genetic.population[father2],quant=1)
            # genetic.population.append(sons.mutation(MUTATION_RATE))

            #replication
            son = Individual(WINDOW_SIZE,chromosome=genetic.population[father1].chromosome)
            genetic.population.append(son.mutation(MUTATION_RATE))

        for individual in genetic.population:
            individual.grade = 0
        

        food_init()
        genetic.generation += 1
        #genetic.population = list(new_population)
        

    pygame.display.update()
    time.tick(fps)
