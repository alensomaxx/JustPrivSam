import numpy as np

arr=np.array([1,2,3,4,5])

print("Orginal Array: ",arr)

arr_add=arr+5
print("Array after adding 5 to each element: ",arr_add)
arr_multiply=arr*5
print("Array after Multiplying 5 to each element: ",arr_multiply)

arr_sum=np.sum(arr)
print("Sum of all elements in the array:", arr_sum)

arr_mean=np.mean(arr)
print("Mean of the array:",arr_mean)
