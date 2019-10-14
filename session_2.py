# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#list
mydata = ['Touka', 'Szulc', 18]

#tuples
perma = ('Touka', 'Szulc', 18)

x = np.array([[1.1, 0.4], 
              [2.2, 1.0], 
              [3.3, 1.5], 
              [4.4, 0.9], 
              [5.5, 2.4]])

y = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
z = np.array([[1.1], [2.2], [3.3], [4.4], [5.5]])

a = np.arange(1.1, 6.6, 1.1)
b = np.linspace(1.1, 5.5, 5, dtype='int')

#%%
import numpy as np

one = np.ones([15])

ones = np.ones([15, 15])
twos = 2*ones

x1 = np.array([1, 2, 3, 4])
x2 = np.array([0.2, 0.4, 0.6, 0.8])

x3 = x1+x2
x4 = x1*2 + 0.5

time = np.arange(0, 1, 0.25)
position = np.sin(2*np.pi*time)

sum = np.sum(position)
sum_across = np.sum(ones, axis=1) #sum across rows
sum_down = np.sum(twos, axis=0) #sum down collumns

data1 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
data2 = data1.transpose()

#%%
import numpy as np
import matplotlib.pyplot as plt

xdata = np.arange(1.1, 5.6, 1.1)
ydata = np.array([0.4, 1.0, 1.5, 0.9, 2.4])
plt.plot(xdata, ydata, 'cx:')

x2data = np.arange(1., 10.1, 1)
y2data = 0.4*x2data
plt.plot(x2data, y2data, 'g')

plt.xlabel()