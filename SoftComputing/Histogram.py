import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000) #Generate 1000 random data proints a=froma  normal distrubution

plt.hist(data, bins=10, color='purple', edgecolor='black', label='Frequency Distribution')

plt.title("Histogram Example")

plt.xlabel('Value')
plt.ylabel('Frequency')

plt.legend()
plt.show()

