import numpy as np
# Define the objective function
def objective_function(x):
    return x ** 2
# Initial nests (solutions)
nests = {
    'Nest 1': -3,
    'Nest 2': 4,
    'Nest 3': 1
}
# Parameters
step_size = 1
random_steps = {
    'Nest 1': 0.5,
    'Nest 2': -0.3,
    'Nest 3': -0.6
}
discovery_rate = 0.25
new_random_value = -2

print("Initial nests:")
for nest, position in nests.items():
    print(f"{nest}: x = {position}, f(x) = {objective_function(position)}")

# Step 1: Generate new solutions using random steps
print("\nNew solutions after Lévy flight:")
new_nests = {}
for nest, position in nests.items():
    new_position = position + step_size * random_steps[nest]
    new_nests[nest] = new_position
    print(f"{nest}: x = {new_position}, f(x) = {objective_function(new_position)}")

# Step 2: Find the worst nest to abandon
worst_nest = max(new_nests, key=lambda nest: objective_function(new_nests[nest]))
print(f"\nWorst nest to abandon: {worst_nest}")

# Step 3: Replace the worst nest with a new random solution
new_nests[worst_nest] = new_random_value
print(f"{worst_nest} is replaced with new random value: x = {new_random_value}, f(x) = {objective_function(new_random_value)}")

# Step 4: Find the best solution
best_nest = min(new_nests, key=lambda nest: objective_function(new_nests[nest]))
print("\nFinal nests after one iteration:")
for nest, position in new_nests.items():
    print(f"{nest}: x = {position}, f(x) = {objective_function(position)}")

print(f"\nBest solution: {best_nest} with x = {new_nests[best_nest]}, f(x) = {objective_function(new_nests[best_nest])}")
