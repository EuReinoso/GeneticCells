# GeneticCells
## A visualization of genetic algorithm.

The main idea of this project is to visualize the behavior of a genetic/evolutionary algorithm in practice.

<img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/default.gif?raw=true" width = "480" height = "360" />

## Explanation

 - First, we want to create a population of individuals that evolve and multiply over time. For this, we create squares that move randomly around the screen.
 
 - We create foods that appear at each generation randomly across the map.
 
 - When collecting the food, the individual's score increases. Individuals who collect more food are more likely to reproduce in the next generation.
 
 - Individuals who do not collect the minimum amount of food will be killed.
 
 - The generated individuals (children) will have a small chance of mutating: increasing or decreasing in size, increasing or decreasing the speed.
 
 Then we will be able to see changes in the population over time.
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/default2.gif?raw=true" width = "480" height = "360" />
 
 Here we can see a significant increase in the speed and size of individuals
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/big.gif?raw=true" width = "480" height = "360" />
 
 ## Graphs
 
 Using the matplotlib library, I created some methods to visualize the population's behavior through graphics.
 
 To open the graphs you can press:
 
 key: s - Avarage sizes/generaton graph.
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/sizes.jpg?raw=true" width = "280" height = "220" />
 
 key: v - Avarage velocityes/generaton graph.
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/velocity.jpg?raw=true" width = "280" height = "220" />
 
 key: g - Avarage grades/generaton graph.
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/grades.jpg" width = "280" height = "220" />
 
 key: p - Individuals/generaton graph.
 
 <img src= "https://github.com/EuReinoso/GeneticCells/blob/master/assets/individuals.jpg?raw=true" width = "280" height = "220" />
 
 ## Final considerations
 
 ### Try changing the variables:
 
 - POPULATION_SIZE - Defines the size of the initial population.
 
 - FOOD_QUANT - Defines the amount of food for each generation.
 
 - MUTATION_RATE - Defines the chance that an individual will mutate.

Watch the changes and have fun!
