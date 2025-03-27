import numpy as np 
import skfuzzy as fuzz 
import matplotlib.pyplot as plt
from skfuzzy import contril as ctrl
#Define Fuzzy Variable
homework= ctrl.Antecedent(np.arange(0, 101, 1), 'homework')
quizzes = ctrl.Antecedent(np.arange(0, 101, 1), 'quizzes')