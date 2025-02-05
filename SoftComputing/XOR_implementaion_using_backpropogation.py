import numpy as np 

def sigmoid(x):
    return 1/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1

np.random.seed(1)

weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)
weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)

learning_rate = 0.1

#training for 100000 iterations
for epoch in range(100000):
    hidden_input = np.dot(x, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    error = y - final_output
    output_error = error 
    output_delta = output_error * sigmoid_derivative(final_output)

    hidden_error = output_delta.dot(weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    weights_hidden_output += hidden_output.T.dot(output_delta)*learning_rate
    weights_input_hidden += x.T.dot(hidden_delta)*learning_rate

    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Error: {np.mean(np.abs(error))}")


print("\n Final Output after training: ")
print(final_output)