from individual import Individual

class Genetic:
    def __init__(self,population_size):
        self.population_size = population_size
        self.population = []
        

    def population_init(self,window_size):
        for i in range(self.population_size):
            population.append(Individual(window_size))