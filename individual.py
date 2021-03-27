from random import random,uniform
from square import Square

MAX_SIZE = 50
MAX_VEL = 5

SIZE_MUTATION = 15
VEL_MUTATION = 5

class Individual:
    def __init__(self,window_size,chromosome=0):
        self.window_size = window_size
        self.chromosome = chromosome

        if chromosome == 0:
            self.chromosome = []
            self.chromosome.append(random() * MAX_SIZE)
            self.chromosome.append(random() * MAX_VEL)
        
        self.square = Square(self.chromosome,window_size)

        self.grade = 0

    def crossover(self,other):
        cut = round(random() * len(self.chromosome))

        son1 = other.chromosome[0:cut] + self.chromosome[cut::]
        son2 = self.chromosome[0:cut] + other.chromosome[cut::]

        sons = [Individual(self.window_size,chromosome=son1),
                Individual(self.window_size,chromosome=son2)]
        
        # sons[0].square.change_rect(son1)
        # sons[1].square.change_rect(son2)

        return sons
    
    def mutation(self,mutation_rate):
        for i in range(len(self.chromosome)):
            if random() < mutation_rate:
                if i == 0:
                    self.chromosome[0] += uniform(-SIZE_MUTATION,SIZE_MUTATION)
                if i == 1:
                    self.chromosome[1] += uniform(-VEL_MUTATION,VEL_MUTATION)
        
        return self



