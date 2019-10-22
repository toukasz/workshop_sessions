# -*- coding: utf-8 -*-
"""
# a)
Name: Touka Szulc
'Coursework 3 - explore Millikan's oil drop experiment'

"""
# b)
import numpy as np
import matplotlib.pyplot as plt

# c)
n = np.arange(4, 19)

# d) (i) type of resulting array: float64
m = np.linspace(4, 18, 15)

# (ii) type of resulting array: int32
h = np.arange(4, 19, 1, int)

# e)
q = np.array([6.558, 8.206, 9.880, 11.50, 13.14, 
              14.82, 16.40, 18.04, 19.68, 21.32, 
              22.96, 24.60, 26.24, 27.88, 29.52])

# f)
plt.plot(n, q, 'c.')

# g)
plt.title('Charge over no. electrons')
plt.xlabel('$n$')
plt.ylabel('$q_n$ / 10$^{-19}$ C')

# h)
m, c = 1.638, 0.0285
besty = m*n + c
plt.plot(n, besty, 'k-')

# i)
plt.legend(('data','best fit'))

# j)
plt.savefig('charge_electron.jpg', dpi=300)

# k) Done!