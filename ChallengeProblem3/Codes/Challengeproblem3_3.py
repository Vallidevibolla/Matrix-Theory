# -*- coding: utf-8 -*-
"""ChallengeProblem3_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xGGcaT6lmL94Yu5YMgCzown-uWdscJKQ
"""

#Code by K.A. Raja Babu 
#June 22,2021
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 100)

y = -1*x**2 + 4*x - 5

plt.plot(x,y,label='y=-$x^2$+4x-5')
plt.grid()


plt.plot(2,-1, 'o')
plt.text(2.2,-0.3,'c')

#show plot
plt.ylim([-15,5])
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend()

plt.show()