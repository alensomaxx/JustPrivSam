import math

data_X=(1.4, 3.7, 8.9, 5.2, 0.9, 1.05, 9.2, 5.9, 6.4, 1.7)
data_Y=(1.3, 3.65, 9.05, 5.3, 1.02, 0.97, 9.15, 5.87, 6.503, 1.609)

#model: Linear --> {(y = m * x + c) <==> y = w * x + b}
m = w = 0.2
c = b = -2

E=0
for i in range (len(data_X)):
    E += math.pow((m * data_X[i] + c) - data_Y[i],2)

E /= len(data_X)

pd_E_wrt_m = 0
for i in range (len(data_X)):
    pd_E_wrt_m += ((m * data_X[i] + c) - data_Y[i]) * data_X[i]
pd_E_wrt_m /= (len(data_X/2))

pd_E_wrt_c = 0
for i in range (len(data_X)):
    pd_E_wrt_c += ((m * data_X[i] + c) - data_Y[i])
pd_E_wrt_c /= (len(data_X/2))
