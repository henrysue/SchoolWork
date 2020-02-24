# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 18:07:12 2019

@author: Henru
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.plot(x,x,label='linear')

plt.legend()

plt.show()