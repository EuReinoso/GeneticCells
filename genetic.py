from individual import Individual
from random import random

class Genetic:
    def __init__(self,population_size):
        self.population_size = population_size
        self.population = []
        self.best_solution = 0 
        self.grade = 0
        

    def population_init(self,window_size):
        for i in range(self.population_size):
            self.population.append(Individual(window_size))
        self.best_solution = self.population[0] #temp

    def best_individual(self):
        for individual in self.population:
            if individual.grade > self.best_solution.grade:
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