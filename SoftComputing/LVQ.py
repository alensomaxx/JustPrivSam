# practical implementation of learning vector quantization
import numpy as np
  #Function to calculate Euclidean distance between two points
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))
  #simplified LVQ model
def lvq(X, y, n_prototypes, learning_rate, n_epochs):
    #step1: Initalize prototypes randomly from dataset
    prototypes = X[:n_prototypes]
    #step2: Train the model(Adjust prototypes)
    for epoch in range(n_epochs):
      for i in range(len(X)):
        data_point = X[i]
        label = y[i]
        # Find the closest prototype to the data point
        distances = [euclidean_distance(data_point, proto) for proto in prototypes]
        closest_prototype_index = np.argmin(distances)
        #step3: update the prototype
        if closest_prototype_index == label:
          #if the prototype belongs to the same class, move it towards the data point
          prototypes[closest_prototype_index] += learning_rate * (data_point - prototypes[closest_prototype_index])
        else:
          prototypes[closest_prototype_index] -= learning_rate * (data_point - prototypes[closest_prototype_index])
        print(f'Epoch {epoch + 1}/{n_epochs} complete.')

    return prototypes

  #simple dataset(2D points with labels)
X = np.array([[5,1.2],[6,1.4],[7,1.8],[8,2.0]])
y = np.array([0, 0, 1, 1])#Labels (0: Class A,1: Class B)

  #parameters
n_prototypes = 2 #one prototype for each class
learning_rate = 0.1
n_epochs = 100 #after a certain point the value is becoming constant([7.52631579 1.90526316])

  #train the LVQ model
prototypes = lvq(X, y, n_prototypes, learning_rate, n_epochs)
  #print the final prototypes
print(f"Final protypes after training: {prototypes}")