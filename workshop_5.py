'''
Computing: Workship 5
Name: Touka Szulc
Date: 11/11/19
'''

x = False
y = [True, True, False]

#%%

x = 1
y = x > 0

#%%

x, y = 1, 2
a = x > 0 and y > 0 #True
b = x < 0 and y > 0 #False
c = x < 0 and y < 0 #False
d = x > 0 and y < 0 #False

#%%

import numpy as np

x = np.arange(1, 7)
logic1 = x > 3

y = 1
logic2 = (x > 3) & (y == 1)

v1 = np.arange(1.5, 10.)
v2 = np.array([1.2, 0.1, 0.5, 1.7, 0.5, 0.7, 0.8, 1.5, 0.4])
keep = v2 > 1
v1keep = v1[keep]
v2keep = v2[keep]

#%%

a_swap, b_swap = np.random.randint(0, 10), np.random.randint(0, 10)

if a_swap > b_swap:
    print('Swap!')
    a_swap, b_swap = b_swap, a_swap
else:
    print('No swap.')

#%%

x = float(input('Please enter a value for x = '))
if x > 10:
    print('x is greater than 10.')
elif x > 5:
    print('x is greater than 5.')
elif x > 0:
    print('x is positive!')