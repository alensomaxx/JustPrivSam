import numpy as np

# defining the perceptron
def perceptron(X, y, learning_rate=0.1, epochs=10):
    weights = np.zeros(X.shape[1])  # Corrected: np.zeros
    bias = 0
    for j in range(epochs):
        print("Epoch: ", j)
        print("Weights: ", weights)
        print("Bias: ", bias)
        for i in range(len(X)):
            summation = np.dot(X[i], weights) + bias  # calculate weighted sum
            prediction = 1 if summation > 0 else 0  # Activation fn (step fn)
            error = y[i] - prediction  # calculating error
            weights = weights + learning_rate * error * X[i]  # update weights
            bias = bias + learning_rate * error  # update bias
    return weights, bias

# sample data for AND operation
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input data
y = np.array([0, 0, 0, 1])  # expected output for AND operation

# train the perceptron
weights, bias = perceptron(X, y)

# testing the perceptron
for x in X:
    summation = np.dot(x, weights) + bias
    prediction = 1 if summation >= 0 else 0  # You can keep >= or just > here.
    print(f"Input: {x}, Prediction: {prediction}")