# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:56:28 2019

@author: Henru
"""
import pandas as pd

nums = pd.Series([1,2,3])

nums.head()

products = np.array([['','product','unit_sold'], [1, 'E-book', 2000],[2, 'Plants', 6000], [3, 'Pencil', 3000]])
product_pf = pd.DataFrame(data=products[1:,1:], # [1:,1:] from first row till end, from first column till end
                          index=products[1:,0], # [1:,0] from first row till end, only first column
                          columns=products[0,1:]) # [1:,0] only first row, form first column till end
print(product_pf)