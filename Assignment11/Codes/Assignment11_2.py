# -*- coding: utf-8 -*-
"""Assignment11_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vcBMw_yjoUCOXNhvoEnl71SMxRmaZqvk
"""

#Plotting x >= -7
#Code by K.A. Raja Babu
#June 19, 2021

import numpy as np
import matplotlib.pyplot as plt

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#vertices
A = np.array([-9, 0])
B = np.array([13, 0])
C = np.array([-7, 0])
D = np.array([0,0])

#Generating and plotting points on number line
X_coord = np.array(np.linspace(-8.0, 12.0, num=21))
Y_coord = np.zeros(21)
plt.plot(X_coord, Y_coord, '|',color='k')

#Generating all lines
x_AB = line_gen(A,B)
x_CB = line_gen(C,B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], color='k',linewidth=1)
plt.plot(x_CB[0,:], x_CB[1,:], color='b', linewidth=2.5,label='x $\geq$ -7')

#Plotting and labelling points
plt.plot(A[0], A[1], '<',color='k')
plt.text(A[0]-1, 0.005, '$-∞$')
plt.plot(B[0], B[1], '>',color='b')
plt.text(B[0], 0.005, '$∞$')
plt.plot(C[0], C[1], 'o',color='b')
plt.text(C[0]-0.5, 0.005 , '$-7$')
plt.text(D[0]-0.2, 0.005 , '$0$')

plt.axis('off')
plt.legend(loc='best')

plt.show()