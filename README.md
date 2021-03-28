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
