# -*- coding: utf-8 -*-
""" Computing - Workshop 4 """

#1 Input from the user
name = input('Enter something: ')

#%%
import numpy as np

nmax = int(input('Enter a maximum integer: '))
power = int(input('Enter the power to use: '))

x = np.arange(1, nmax+1)
print(x**power)

#%%
#2 Printing out text

x_1 = float(input('Enter value of \'x\': '))
y = x_1**2

print('Square of {0:.2f} is {1:.2f}.' .format(x_1, y))

#%%
#3 Random numbers
#3.1 Uniform distributions

import numpy as np
import matplotlib.pyplot as plt

uniform = np.sort(np.random.random_sample(100))

#plt.plot(uniform, '.')

plt.hist(uniform, bins=20)

#%%

import numpy as np
import matplotlib.pyplot as plt

r = np.random.random_integers(1, 6, 1000)
b = np.linspace(0.5, 6.5, 7)

plt.hist(r, bins=b)

#%%
#3.2 Normal (Gaussian) distributions

import numpy as np
import matplotlib.pyplot as plt

normal = np.sort(np.random.normal(size=500, loc=100, scale=15))

#plt.plot(normal)

plt.hist(normal, bins=20, density=True)

mu = np.mean(normal)
stdv = np.std(normal)

print('mu = {0:.2f}, stdv = {1:.2f}'.format(mu, stdv))

#%%
#4 Exercises
#4.1 Test your use of 'input'

print('Typical parameters:')
print('m ~ 5, b ~ 0.5, w_0 ~ 1')
m = input('Mass = ')
b = input('Damping term = ')
w_0 = input('Natural oscillation frequency = ')

w = np.random.uniform(0.5, 1.5, 200)

A = (m**2 * (w_0**2 - w**2)**2 + b**2 * w**2)**-0.5

plt.plot(w, A, 'c.')