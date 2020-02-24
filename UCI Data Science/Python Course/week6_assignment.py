#!/usr/bin/env python
# coding: utf-8

# In[ ]:


my_date_str = '20170817'

from datetime import datetime, timedelta

def days_15(my_date_str):
    dtObj = datetime.strptime(my_date_str,'%Y%m%d')
    day = timedelta(days=1)
    datelist = [dtObj + day * i for i in range(16)]
    return(datelist)
result = days_15(my_date_str)
print(result)


# In[ ]:


from glob import glob
import os

glob_pattern = 'C:\\Users\\Henru\\Desktop\\Python Course\\Test\\logData_*.txt'

def count_files(x):
    files = glob(x)
    return len(files)
num_files = count_files(glob_pattern)
print(num_files)

