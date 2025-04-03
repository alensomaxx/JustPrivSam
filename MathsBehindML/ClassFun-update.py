import math
import numpy as np
import matplotlib.pyplot as plt

def linear_regression(data_X, data_Y, learning_rate=0.01, iterations=1000, regularization='none', lambda_val=0.1, feature_scaling='none', polynomial_degree=1, train_test_split_ratio=0.8, early_stopping=False, validation_split_ratio=0.2, plot_results=False):
    """
    Performs linear regression with various options and plotting capabilities.
    """

    X = np.array(data_X)
    Y = np.array(data_Y)

    # Polynomial Feature Transformation
    if polynomial_degree > 1:
        X_poly = np.column_stack([X**i for i in range(1, polynomial_degree + 1)])
    else:
        X_poly = X.reshape(-1, 1)

    # Feature Scaling
    if feature_scaling == 'normalize':
        X_min = np.min(X_poly, axis=0)
        X_max = np.max(X_poly, axis=0)
        X_scaled = (X_poly - X_min) / (X_max - X_min)
    elif feature_scaling == 'standardize':
        X_mean = np.mean(X_poly, axis=0)
        X_std = np.std(X_poly, axis=0)
        X_scaled = (X_poly - X_mean) / X_std
    else:
        X_scaled = X_poly

    # Train-Test Split
    split_index = int(len(X_scaled) * train_test_split_ratio)
    X_train, X_test = X_scaled[:split_index], X_scaled[split_index:]
    Y_train, Y_test = Y[:split_index], Y[split_index:]

    if early_stopping:
        validation_split = int(len(X_train) * (1 - validation_split_ratio))
        X_val, X_train = X_train[validation_split:], X_train[:validation_split]
        Y_val, Y_train = Y_train[validation_split:], Y_train[:validation_split]

    # Initialize weights and bias
    weights = np.zeros(X_train.shape[1])
    bias = 0

    # Gradient Descent
    best_val_error = float('inf')
    best_weights = weights.copy()
    best_bias = bias
    no_improvement_count = 0
    errors = []  # For plotting the error over iterations
    weight_history = []  # For plotting weight changes

    for _ in range(iterations):
        predictions = np.dot(X_train, weights) + bias
        error = predictions - Y_train
        errors.append(np.mean(error**2))  # Save error for plotting
        weight_history.append(weights.copy())  # Save weights

        # Calculate gradients
        grad_weights = (1 / len(X_train)) * np.dot(X_train.T, error)
        grad_bias = (1 / len(X_train)) * np.sum(error)

        # Regularization
        if regularization == 'l1':
            grad_weights += lambda_val * np.sign(weights)
        elif regularization == 'l2':
            grad_weights += 2 * lambda_val * weights

        # Update weights and bias
        weights -= learning_rate * grad_weights
        bias -= learning_rate * grad_bias

        if early_stopping:
            val_predictions = np.dot(X_val, weights) + bias
            val_error = np.mean((val_predictions - Y_val) ** 2)
            if val_error < best_val_error:
                best_val_error = val_error
                best_weights = weights.copy()
                best_bias = bias
                no_improvement_count = 0
            else:
                no_improvement_count += 1
                if no_improvement_count > 10:
                    weights = best_weights.copy()
                    bias = best_bias
                    break

    # Evaluation
    predictions_test = np.dot(X_test, weights) + bias
    mse = np.mean((predictions_test - Y_test) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(predictions_test - Y_test))
    ss_res = np.sum((predictions_test - Y_test) ** 2)
    ss_tot = np.sum((Y_test - np.mean(Y_test)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    if plot_results:
        plt.figure(figsize=(18, 6))

        # Plot 1: Actual vs. Predicted
        plt.subplot(1, 3, 1)
        plt.scatter(X_test[:, 0], Y_test, label='Actual Data')
        plt.scatter(X_test[:, 0], predictions_test, label='Predicted Data')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Actual vs. Predicted')
        plt.legend()

        # Plot 2: Error over Iterations
        plt.subplot(1, 3, 2)
        plt.plot(errors)
        plt.xlabel('Iterations')
        plt.ylabel('Mean Squared Error')
        plt.title('Error over Iterations')

        # Plot 3: Weight Changes
        plt.subplot(1, 3, 3)
        for i in range(X_train.shape[1]):
            weight_values = [w[i] for w in weight_history]
            plt.plot(weight_values, label=f'Weight {i+1}')
        plt.xlabel('Iterations')
        plt.ylabel('Weight Value')
        plt.title('Weight Changes over Iterations')
        plt.legend()

        plt.tight_layout()
        plt.show()

    return {
        'weights': weights,
        'bias': bias,
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'r_squared': r_squared
    }

# Example Usage with Menu
data_X = (1.4, 3.7, 8.9, 5.2, 0.9, 1.05, 9.2, 5.9, 6.4, 1.7)
data_Y = (1.3, 3.65, 9.05, 5.3, 1.02, 0.97, 9.15, 5.87, 6.503, 1.609)

# Menu System
learning_rate = float(input("Enter learning rate (e.g., 0.01): "))
iterations = int(input("Enter number of iterations: "))
regularization = input("Enter regularization ('none', 'l1', 'l2'): ")
lambda_val = float(input("Enter lambda value (for regularization): "))
feature_scaling = input("Enter feature scaling ('none', 'normalize', 'standardize'): ")
polynomial_degree = int(input("Enter polynomial degree: "))
train_test_split_ratio = float(input("Enter train-test split ratio (e.g., 0.8): "))
early_stopping_choice = input("Use early stopping? (yes/no): ").lower()
early_stopping = early_stopping_choice == 'yes'
validation_split_ratio = 0.2
if early_stopping:
    validation_split_ratio = float(input("Enter validation split ratio: "))
plot_choice = input("Plot the results? (yes/no): ").lower()
plot_results = plot_choice == 'yes'

results = linear_regression(data_X, data_Y, learning_rate, iterations, regularization, lambda_val, feature_scaling, polynomial_degree, train_test_split_ratio, early_stopping, validation_split_ratio, plot_results)

print("\nResults:")
print(f"Weights: {results['weights']}")
print(f"Bias: {results['bias']}")
print(f"MSE: {results['mse']}")
print(f"RMSE: {results['rmse']}")
print(f"MAE: {results['mae']}")
print(f"R-squared: {results['r_squared']}")