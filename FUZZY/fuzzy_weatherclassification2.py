import numpy as np
import matplotlib.pyplot as plt 
import skfuzzy as fuzz

# Define the ranges
temperature = np.arange(0, 41, 1)
humidity = np.arange(30, 71, 1)
windspeed = np.arange(5, 21, 1)

# Fuzzy membership functions for humidity
low_humid = fuzz.trimf(humidity, [30, 40, 50])
mid_humid = fuzz.trimf(humidity, [40, 50, 60])
high_humid = fuzz.trimf(humidity, [50, 60, 70])

# Fuzzy membership functions for temperature
low_temp = fuzz.trimf(temperature, [0, 0, 20])
mid_temp = fuzz.trimf(temperature, [15, 25, 35])
high_temp = fuzz.trimf(temperature, [30, 40, 40])

# Fuzzy membership functions for windspeed
low_wind = fuzz.trimf(windspeed, [5, 5, 10])
mid_wind = fuzz.trimf(windspeed, [8, 12, 16])
high_wind = fuzz.trimf(windspeed, [14, 20, 20])

# Plotting fuzzy temperature classification
plt.figure(figsize=(10, 5))
plt.plot(temperature, low_temp, label='Cold', color='blue')
plt.plot(temperature, mid_temp, label='Warm', color='orange')
plt.plot(temperature, high_temp, label='Hot', color='red')
plt.title("Fuzzy Temperature Classification")
plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.grid()
plt.legend()
plt.show()

# Weather classification function
def classify_weather(temp, wind_speed, humid):
    # Temperature degrees
    low_temp_degree = fuzz.interp_membership(temperature, low_temp, temp)
    mid_temp_degree = fuzz.interp_membership(temperature, mid_temp, temp)
    high_temp_degree = fuzz.interp_membership(temperature, high_temp, temp)
    
    # Wind speed degrees
    low_wind_degree = fuzz.interp_membership(windspeed, low_wind, wind_speed)
    mid_wind_degree = fuzz.interp_membership(windspeed, mid_wind, wind_speed)
    high_wind_degree = fuzz.interp_membership(windspeed, high_wind, wind_speed)
    
    # Humidity degrees
    low_humid_degree = fuzz.interp_membership(humidity, low_humid, humid)
    mid_humid_degree = fuzz.interp_membership(humidity, mid_humid, humid)
    high_humid_degree = fuzz.interp_membership(humidity, high_humid, humid)

    # Fuzzy rules for weather classification
    sunny_score = high_temp_degree * low_wind_degree * low_humid_degree
    cloudy_score = mid_temp_degree * mid_wind_degree * mid_humid_degree
    rainy_score = low_temp_degree * high_wind_degree * high_humid_degree

    # Determine the highest score
    if sunny_score > cloudy_score and sunny_score > rainy_score:
        return "SUNNY"
    elif cloudy_score > sunny_score and cloudy_score > rainy_score:
        return "CLOUDY"
    else:
        return "RAINY"

# Get user input
temp = int(input("Enter Temperature (0-40): "))
humid = int(input("Enter value for Humidity (30-70): "))
wind_speed = int(input("Enter value for Wind Speed (5-20): "))

# Classify weather
result = classify_weather(temp, wind_speed, humid)
print("Weather is: ", result)
