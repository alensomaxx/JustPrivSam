import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#Define the universe of discourse (Temperature range from 0 to 50)
temperature = np.arange(0,51,1)
print("Crisp set for temp: ",temperature)

#Defineinf fuzzy memebership function for temperature

cold = fuzz.trimf(temperature, [0,0,20])
warm = fuzz.trimf(temperature, [21,25,35])
hot = fuzz.trimf(temperature, [36,40,50])

plt.figure(figsize=(10,5))
plt.plot(temperature, cold, label='Cold',color='blue')
plt.plot(temperature, warm, label='Warm',color='orange')
plt.plot(temperature, hot, label='Hot',color='red')
plt.title("Fuzzy Membership Function for Weather Classification")
plt.xlabel("Temperature")
plt.ylabel("Memebership Degree")
plt.grid()
plt.legend()
plt.show()

#defuzzification

input_temp=int(input("Enter temp btw 0 to 50: "))

cold_level=fuzz.interp_membership(temperature, cold, input_temp)
warm_level=fuzz.interp_membership(temperature, warm, input_temp)
hot_level=fuzz.interp_membership(temperature, hot, input_temp)

print("Temperature: ",input_temp)
print(f"Cold Membership level: {cold_level:.2f}")
print(f"Warm Membership level: {warm_level:.2f}")
print(f"Hot Membership level: {hot_level:.2f}")

#Determine classification based on highest membership level
if cold_level > warm_level and cold_level > hot_level:
    print("Classification: Cold")
elif warm_level > cold_level and warm_level > hot_level:
    print("Classification: Warm")
else:
    print("Classification: Hot")