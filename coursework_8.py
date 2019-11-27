"""
Coursework Set 8:
Name: Touka Szulc
Date: 27/22/19
"""
import numpy as np

#1 - Defining arrays:
#a)
results = np.array([(54, 1, 0), (56, 0, 1), (72, 0, 0), (34, 3, 0)])
names = np.array(['Amy', 'Bob', 'Carol', 'Dave'])

#b) (i) - True = pass, False = fail
notfail = results[:, 2] == 0

#  (ii) - Extracted data & name of those who failed.
fail = results[np.invert(notfail)]
f_names = names[np.invert(notfail)]

#c) - Ask no. 1 - 4, store as int:
nth = int(input('Input nth value: ')) - 1
print('Name:', names[nth], '\nData:', results[nth])

#%%

#2 - Calculating roots of quadratics:
#a) - Input values
print('\nGiven \'f(x) = ax^2 + bx + c = 0\';\n'
      'where a, b, c are non-zero coefficients:')
a, b, c = float(input('a = ')), float(input('b = ')), float(input('c = '))

#b) - Determinant determination
d = b**2 - 4*a*c

#c)  (i) -  discriminant > 0
print('\nb^2 - 4ac > 0 is', d > 0)

#   (ii) -  discriminant = 0
print('b^2 - 4ac = 0 is', d == 0)

#  (iii) -  discriminant < 0
print('b^2 - 4ac < 0 is', d < 0)

print('\nb^2 - 4ac =', b**2 - 4*a*c,'\n')

if d > 0:
    print('Since it has two real and different roots:\n'
          'x ≈ ', (-b + (b**2 - 4*a*c)**.5)/(2*a),
          'or', (-b - (b**2 - 4*a*c)**.5)/(2*a))
elif d == 0:
    print('Since it has one pair of equal roots:\n'
          'x ≈ ', (-b + (b**2 - 4*a*c)**.5)/(2*a))
else:
    print('No real roots (two complex roots)! So in complex form:') 
    
    #d) Calculation via Numpy's "roots" function.
    print('x =', np.roots((a, b, c))[0], 'or', np.roots((a, b, c))[1])