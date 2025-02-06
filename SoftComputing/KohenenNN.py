import numpy as np

def calculate_bmu(input_vector, weights):
    distances = np.linalg.norm(weights - input_vector, axis=1)#Euclidean distances from the input vector
    bmu_index = np.argmin(distances)#index of the minimum distance
    return bmu_index

if __name__ == "__main__":
    input_vector = np.array([0.5, 0.2])
    weights = np.array(([0.1,0.2], [0.4,0.5], [0.6,0.1]))

    bmu_index = calculate_bmu(input_vector, weights)
    print(f"The index of the best matching unit is : {bmu_index}")
