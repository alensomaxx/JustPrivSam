'''import pandas as pd
import matplotlib.pyplot as pt

y=pd.read_csv("Happinessidex.xlsx")

print(y)
'''

import pandas as pd
import matplotlib.pyplot as plt  # Corrected import

y = pd.read_csv('happyProject.xlsx') 

print(y) 

# To get specific details, you can use indexing and column selection:

# 1. Get the first 5 rows
print(y.head()) 

# 2. Get the last 5 rows
print(y.tail())

# 3. Get the column names
print(y.columns)

# 4. Get the number of rows and columns
print(y.shape) 

# 5. Get information about the DataFrame
print(y.info())

# 6. Get summary statistics 
print(y.describe()) 

# To plot data (example: a simple bar chart)
# plt.bar(y['Country'], y['Score']) 
# plt.xlabel('Country')
# plt.ylabel('Happiness Score')
# plt.title('Happiness Scores by Country')
# plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
# plt.show()