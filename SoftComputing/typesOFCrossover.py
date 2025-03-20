import random

#One-Point Crossover

def one_point_crossover(parent1, parent2):
    #Select a random crossover point
    point = random.randint(0, len(parent1) - 1)
    #Create the first child
    child1 = parent1[:point] + parent2[point:]
    #Create the second child
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

#Two-Point Crossover

def two_point_crossover(parent1, parent2):
    #Random crossover points
    point1 = random.randint(0, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)

    #Perform the corssover

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2


#Uniform Crossover
def uniform_crossover(parent1, parent2):
    child1 = []
    child2 = []

    for i in range(len(parent1)):
        if random.random() < 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])

    return child1, child2

#Testing the crossover functions


parent2 = [0, 1, 0, 1, 0]
parent1 = [1, 0, 1, 0, 1]

    #Perform One-Point Crossover
child1, child2 = one_point_crossover(parent1, parent2)
print("One-Point Crossover:")
print(f"Parent1: {parent1}")
print(f"Parent2: {parent2}")
print(f"Child1: {child1}")
print(f"Child2: {child2}")

    #Perform Two-Point Crossover
child1, child2 = two_point_crossover(parent1, parent2)
print("\nTwo-Point Crossover:")
print(f"Parent1: {parent1}")
print(f"Parent2: {parent2}")
print(f"Child1: {child1}")
print(f"Child2: {child2}")