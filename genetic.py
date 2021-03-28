from individual import Individual
from random import random

STARVE = 5

class Genetic:
    def __init__(self,population_size):
        self.population_size = population_size
        self.population = []
        self.best_solution = 0 
        self.grade = 0
        self.generation = 1
        

    def population_init(self,window_size):
        for i in range(self.population_size):
            self.population.append(Individual(window_size))
        self.best_solution = self.population[0] #temp

    def population_order(self):
        self.population = sorted(self.population,
                                key= lambda population:population.grade,
                                reverse = True)
    
    def best_individual(self,individual):
        self.best_solution = individual

    def population_assessment(self,):
        grade = 0
        for individual in self.population:
            grade += individual.grade
        return grade
    
    def father_select(self,pop_assessment):
        father = -1
        valor = random() * pop_assessment
        total = 0
        i = 0
        while i < len(self.population) and total < valor:
            father += 1
            total += self.population[i].grade
            i += 1
        return father

    def starve_kill(self):
        i = 0
        flag = False
        while i < len(self.population):
            if flag:
                flag = False
            if self.population[i].grade < STARVE:
                self.population.pop(i)
                i = 0
                flag = True
            if not flag:
                i += 1

    def avarage(self):
        total_size = 0
        total_vel = 0
        total_grade = 0
        
        for individual in self.population:
            total_size += round(individual.square.rect.width)
            total_vel += round(individual.square.vel_x)
            total_grade += individual.grade

        avarage_size = total_size/len(self.population)
        avarage_vel = total_vel/len(self.population)
        avarage_grade = total_grade/len(self.population)

        return avarage_size, avarage_vel, avarage_grade

    