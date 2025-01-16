import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1,2], [3,4],[5,6]])
print(a)

b=2*a
print (b)

plt.plot(a[::,:1:], a[::, 1::])

plt.show()
'''
c=np.linspace(0, 2*np.pi, 100)
print(type(c))
print(c)

plt.plot(c, np.sin(c))
plt.plot(c, np.cos(c))

plt.show()

'''