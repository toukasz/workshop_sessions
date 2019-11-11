import numpy as np
import matplotlib.pyplot as plt

n = int(input('n = '))
x = np.random.rand(n) * 2 - 1
y = np.random.rand(n) * 2 - 1

plt.plot(x, y, 'g.')

line = np.arange(-1, 1, 0.001)
c = np.sqrt(1 - line**2)

plt.plot(line, c, 'r')
plt.plot(line, -c, 'r')

r = (x**2 + y**2)**.5
r_in = r[r <= 1]

tot = len(r)
inn = len(r_in)

pi = 4 * (inn / tot)
print('pi ~ {:.9}' .format(pi))