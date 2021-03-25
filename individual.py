from random import random,randrange
from square import Square

MAX_SIZE = 50
MAX_VEL = 10

SIZE_MUTATION = 3
VEL_MUTATION = 1

class Individual:
    def __init__(self,window_size):
        self.window_size = window_size
        self.chromosome = []

        self.chromosome.append(random() * MAX_SIZE)
        self.chromosome.append(random() * MAX_VEL)

        self.square = Square(self.chromosome,window_size)

    def crossover(self,other):
        cut = round(random() * len(self.chromosome))

        son1 = other.chromosome[0:cut] + self.chromosome[cut::]
        son2 = self.chromosome[0:cut] + other.chromosome[cut::]

        sons = [Individual(self.window_size),
                Individual(self.window_size)]
        
        sons[0].chromosome = son1
        sons[1].chromosome = son2

        return sons
    
    def mutation(self,mutation_rate):
        for i in range(self.chromosome):
            if random() < mutation_rate:
                if i == 0:
                    self.chromosome[0] += randrange(-SIZE_MUTATION,SIZE_MUTATION,0.1)
                if i == 1:
                    self.chromosome[1] += randrange(-VEL_MUTATION,VEL_MUTATION,0.1)
        
        return self


    