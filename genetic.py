from individual import Individual

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

    def best_individual(self,individual):
        if individual.grade > self.best_solution.grade:
            self.best_solution = individual

    def population_assessment(self,):
        grade = 0
        for individual in self.population:
            grade += individual.grade
        return grade