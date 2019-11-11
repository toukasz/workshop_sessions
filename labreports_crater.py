# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

datax = np.array([12, 24, 36, 48, 60, 72, 84, 96])
datay = np.array([3.0, 3.3, 53/15, 3.8, 127/30, 13/3, 89/20, 4.9])

yerror = np.array((0.25*(3**(-1/2)))/datay)

logx = np.log(datax)
logy = np.log(datay)

xbar = np.mean(logx)
ybar = np.mean(logy)
N = len(logx)

#The Least Squares Criterion
numerator = np.sum((logx - xbar)*logy)
denominator = np.sum((logx - xbar)**2)
m = numerator / denominator
c = ybar - m * xbar

sigmam = np.sqrt(np.sum((logy-m*logx-c)**2)/((N-2)*np.sum((logx-xbar)**2)))
sigmac = np.sqrt((np.sum((logy-m*logx-c)**2)/(N-2))*((1/N)+(xbar**2/np.sum((logx-xbar)**2))))

print("gradient is: {0:.6f} +/- {1:.6f}". format(m, sigmam))
print("intercept is: {0:.6f} +/- {1:.6f}". format(c, sigmac))

plt.errorbar(logx, logy, yerr=yerror, fmt='.', color='k', capsize=2, ecolor='k')
plt.plot(logx, m*logx + c, color = 'k')

plt.yticks(fontsize = 8)
plt.xticks(fontsize = 8)

plt.xlabel('$log(x)$', fontsize = 9)
plt.ylabel('$log(y)$', fontsize = 9)
plt.title('$Fig. 2$', fontsize = )

plt.savefig("labrep_graph.jpg", dpi=300)

plt.show()