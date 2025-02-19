import numpy as np

# Radial Basis Function (RBF)

def rbf(x, c, r):
    return np.exp(- (x-c)*2 / r*2)

# Simple example to train the network and make predictions

def main():
    # Training data: Input (X_train) and output (y_train)
    X_train = np.array([0.1, 0.4, 0.9, 1.0])
    y_train = np.array([0.5,1.0, 0.8, 1.2])

    #Centers (we select two centres from the training data)
    centers = np.array([0.1, 0.9]) # Two centers
    r = 0.2 #Spread value (radius)

    # Step 1: Calculate the activation matrix Phi
    Phi = np.array([[rbf(x, centers[0], r), rbf(x, centers[1], r)] for x in X_train])

    #Step 2: Solve for weights using a direct apprach (withour inversion)
    # Use np.linalg.lstsq (Least Squares method) which solves the equation without inversion

    weights, _, _, _ = np.linalg.lstsq(Phi, y_train, rcond=None)

    # Step 3: Make predictions using the learned weights
    X_test = np.array([0.4, 0.7])
    predictions = np.array([np.sum([rbf(x, centers[0], r), rbf(x, centers[1], r)] * weights) for x in X_test])

    # Print predictions

    print("Weights: ", weights)
    print("Predictions: ", predictions)


main()