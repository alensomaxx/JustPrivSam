import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y=[5,7,9,11,13]

plt.scatter(x,y, color='red', marker ='x', label ='Data Points')


plt.title("Scatter Plot Example")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()
plt.show()