# -*- coding: utf-8 -*-
"""Assignment4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-B8AW11yoY9zNQv30ZB3_rAEwQPV0r-0
"""

#Code by K.A. Raja Babu
#May 21, 2021
#Plotting a line 

import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #referred from G.V.V sir's Code

#Inputs
n = np.array([1,1]) 
c1 = (-21/5)
c2= (7/3)
e1 = np.array([1,0]) 
e2 = np.array([0,1]) 
A = c1*e1
B = c2*e2

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1+0.03) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()