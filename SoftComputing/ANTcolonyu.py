import numpy as np
def calculate_probabilities(pheromones, distances, alpha = 1.0, beta = 2.0 ):
  pheromone_factor = pheromones ** alpha
  heuristic_factor = (1.0 / distances) ** beta
  combined_factor = pheromone_factor * heuristic_factor
  return combined_factor / np.sum(combined_factor)

def update_pheromones(pheromones, chosen_path, decay = 0.1, reward = 1.0):
  pheromones *= (1 - decay)
  pheromones[chosen_path] += reward
  return pheromones

def main():
  n_paths = 4
  pheromones = np.array([1.0, 2.0, 1.5, 0.5])
  distances = np.array([10, 20, 15, 25])
  print(f"Initial Pheromones: {pheromones}")
  for i in range(10):
    probabilities = calculate_probabilities(pheromones, distances)
    chosen_path = np.random.choice(n_paths, p = probabilities)
    pheromones = update_pheromones(pheromones, chosen_path)
    print(f"Iteration{i + 1}: Probabilities{probabilities}, Chosen Path {chosen_path + 1}, Updated Pheromones: {pheromones}")

main()