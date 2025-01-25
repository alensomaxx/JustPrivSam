import pandas as pd
import matplotlib.pyplot as plt  # Corrected import


y = pd.read_csv('happyProject.csv') 

print(y) 


#Get the number of rows and columns
print(y.shape) 

#Get information about the DataFrame
print(y.info())

#Get summary statistics 
print(y.describe()) 

# To plot data
plt.scatter(y['Health Index'],y['Happiness Index'], color='red', marker ='x', label ='Health - Happiness')
#plt.bar(y['Health Index'], y['Happiness Index']) 
plt.xlabel('Health Index')
plt.ylabel('Happiness Index')
plt.title('Index Comparison')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()