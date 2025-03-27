import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


#Define fuzzy variables

homework = ctrl.Antecedent(np.arange(0, 101, 1), 'homework')
quizzes = ctrl.Antecedent(np.arange(0, 101, 1), 'quizzes')
attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
final_grade = ctrl.Consequent(np.arange(0, 101, 1), 'final_grade')

#Membership function

homework['low'] = fuzz.trimf(homework.universe, [0, 0, 50])
homework['medium'] = fuzz.trimf(homework.universe, [30, 60, 90])
homework['high'] = fuzz.trimf(homework.universe, [50, 100, 100])

quizzes['low'] = fuzz.trimf(quizzes.universe, [0, 0, 50])
quizzes['medium'] = fuzz.trimf(quizzes.universe, [30, 60, 90])
quizzes['high'] = fuzz.trimf(quizzes.universe, [50, 100, 100])


attendance['low']= fuzz.trimf(attendance.universe, [0, 0, 50])
attendance['medium']= fuzz.trimf(attendance.universe, [30, 60, 90])
attendance['high']= fuzz.trimf(attendance.universe, [50, 100, 100])

final_grade['low'] = fuzz.trimf(final_grade.universe, [0, 0, 50])
final_grade['medium'] = fuzz.trimf(final_grade.universe, [30, 60, 90])
final_grade['high'] = fuzz.trimf(final_grade.universe, [50, 100, 100])

#define fuzzy rules

rule1 = ctrl.Rule(homework['high'] & quizzes['high'] & attendance['high'], final_grade['high'])
rule2 = ctrl.Rule(homework['medium'] | quizzes['medium'] | attendance['medium'], final_grade['medium'])
rule3 = ctrl.Rule(homework['low'] | quizzes['low'] | attendance['low'], final_grade['low'])

#control system

grade_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
grade_system = ctrl.ControlSystemSimulation(grade_ctrl)

#example input

grade_system.input['homework'] = 80
grade_system.input['quizzes'] = 90
grade_system.input['attendance'] = 100

#compute output

grade_system.compute()

#print output

print(f"Predicted Final Grade: {grade_system.output['final_grade']}%")