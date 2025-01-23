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
# plt.bar(y['Country'], y['Score']) 
# plt.xlabel('Country')
# plt.ylabel('Happiness Score')
# plt.title('Happiness Scores by Country')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.show()