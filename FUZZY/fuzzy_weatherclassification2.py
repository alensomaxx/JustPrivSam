import numpy as np
import matplotlib.pyplot as plt 
import skfuzzy as fuzz

temperature = np.arange(0,41,1)
humidity = np.arange(30,70,1)
windspeed = np.arange(5,21,1)


low_humid = fuzz.trimf(humidity,[30,40,50])
mid_humid = fuzz.trimf(humidity,[40,50,60])
high_humid = fuzz.trimf(humidity,[50,60,70])


low_temp = fuzz.trimf(temperature,[0,0,20])
mid_temp = fuzz.trimf(temperature,[15,25,35])
high_temp = fuzz.trimf(temperature,[30,40,40])

low_wind = fuzz.trimf(temperature,[5,5,10])
mid_wind= fuzz.trimf(temperature,[8,12,16])
high_wind= fuzz.trimf(temperature,[14,20,20])

plt.figure(figsize=(10,5))
plt.plot(temperature, low_temp, label='Cold',color='blue')
plt.plot(temperature, mid_temp, label='Warm',color='orange')
plt.plot(temperature, high_temp, label='Hot',color='red')
plt.title("Fuzzy Temperature Classification")
plt.xlabel("Temperature")
plt.ylabel("Memebership Degree")
plt.grid()
plt.legend()
plt.show()


def classify_weather(temp,wind_speed, humid):
    low_temp_degree=fuzz.interp_membership(temperature, low_temp, temp)
    mid_temp_degree=fuzz.interp_membership(temperature, mid_temp, temp)
    high_temp_degree=fuzz.interp_membership(temperature, high_temp, temp)
    
    
    low_wind_degree=fuzz.interp_membership(temperature, low_wind, temp)
    mid_wind_degree=fuzz.interp_membership(temperature, mid_wind, temp)
    high_wind_degree=fuzz.interp_membership(temperature, high_wind, temp)

    
    low_humid_degree=fuzz.interp_membership(temperature, low_humid, temp)
    mid_humid_degree=fuzz.interp_membership(temperature, mid_humid, temp)
    high_humid_degree=fuzz.interp_membership(temperature, high_humid, temp)

    sunny_score = (high_temp_degree * low_wind_degree * low_humid_degree)
    cloudy_score = (mid_temp_degree * mid_wind_degree * mid_humid_degree)
    rainy_score = (low_temp_degree * high_wind_degree * high_humid_degree)

    if sunny_score > cloudy_score and sunny_score > rainy_score:
        return "SUNNY"
    elif cloudy_score > sunny_score and cloudy_score > rainy_score:
        return "RAINY"
    
temp=int(input("Enter Temperature(0-40): "))
humid=int(input("Enter value for Humidity(30-70): "))
wind_speed=int(input("Enter value for Wind Speed(5-20): "))

result=classify_weather(temp,humid,wind_speed)

print("Weather is : ",result)