import random
#Function to calculate fitness (just return the vlaue at fitness)

def fitness_fucntion(individual):
    return individual #Fitness is the individual's value (higher is better)

#Roulette Wheel Selection Function

def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values) #Total fitness of the population
    pick = random.uniform(0, total_fitness) #Pick a random point between 0 and t
    current_sum = 0
    for i, fitness in enumerate(fitness_values):
        current_sum += fitness
        if current_sum > pick:
            return population[i]

#Create a population of individuals (vlaues from 1 to 10)
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Calculate firness values for the population
fitness_values = [fitness_fucntion(ind) for ind in population]

#Perform roulette wheel selection
selected_individual = roulette_wheel_selection(population, fitness_values)

#Output the selected individual
print(f"Selected Individual: {selected_individual}")