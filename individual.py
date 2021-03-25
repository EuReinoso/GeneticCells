import random
from square import Square

MAX_SIZE = 50
MAX_VEL = 10

class Individual:
    def __init__(self,window_size):
        self.chromosome = []

        self.chromosome.append(random.random() * MAX_SIZE)
        self.chromosome.append(random.random() * MAX_VEL)

        self.square = Square(self.chromosome,window_size)

    