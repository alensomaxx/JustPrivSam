import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#Define fuzzy varibales
age = ctrl.Antecedent(np.arrange(0, 101, 1), 'age') #age as input
activity = ctrl.Consequent(np.arrange(0, 11, 1), 'activity') #Activity level as output

# Step4: Define fuzzy membership fns for age
age['young'] = fuzz.trimf(age.universe, [0,0,30])
age['adult'] = fuzz.trimf(age.universe, [20,40,60])
age['senior'] = fuzz.trimf(age.universe, [50,100,100])

activity['low'] = fuzz.trimf(activity.universe, [0,0,3])
activity['medium'] = fuzz.trimf(activity.universe, [2,5,8])
activity['high'] = fuzz.trimf(activity.universe, [0,0,3])


age.view()

plt.draw()
plt.show() 