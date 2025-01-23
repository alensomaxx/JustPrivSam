import numpy as np

array = np.arange(9)
print ("Orginal Array: ",array)


reshaped_array=array.reshape(3,3)
print("Reshaped Array (3X3): \n", reshaped_array)

sliced_array = reshaped_array[1:,1:]
print("Sliced Portion of array: \n",sliced_array)

#Transpose the 2D array (swap rows and columns)
transposed_array = reshaped_array.T
print("Transposed Array: \n",transposed_array)