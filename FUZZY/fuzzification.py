import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#Define the universe of discourse (input range of temperature)
temperature = np.arange(0,41,1) #values from 0 to 40
print ("Crisp set temperature :", temperature)

#Fuzzification methods

#1. Triangular Membership function
temp_triangular = fuzz.trimf(temperature, [10,20,30])
print("Fuzzy set tri mv:", temp_triangular)

#2.Trapezoidal Mambership Function
temp_trapezodial = fuzz.trapmf(temperature,[10,15,25,30])
print("Fuzzy Set trap mv:",temp_trapezodial)


#3.Gaussian Mambership Function
temp_gaussian = fuzz.gaussmf(temperature,20,5) #mean = 20 , sigma = 5
print("Fuzzy Set gau mv:",temp_gaussian)

plt.figure(figsize =(10,6))

#Plot for triangular membership function
plt.plot(temperature, temp_triangular, label="Triangular", color = "blue")
plt.title("Triangular Membership Function for temperature")
plt.xlabel("Temperature:(^C)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()

#Plot for Trapezoidal membership function
plt.plot(temperature, temp_trapezodial, label="Trapezoidal", color = "red")
plt.title("Trapezoidal Membership Function for temperature")
plt.xlabel("Temperature:(^C)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()

#Plot for Gaussian membership function
plt.plot(temperature, temp_gaussian, label="Gaussian", color = "green")
plt.title("Gaussian Membership Function for temperature")
plt.xlabel("Temperature:(^C)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(True)
plt.show()