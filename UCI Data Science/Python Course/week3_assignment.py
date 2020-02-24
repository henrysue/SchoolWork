#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for var in range(10):
    print(var)


# In[ ]:


for x in range(10):
    print(x)
    if x == 0:
        print('Zero')
    elif x%2 == 0:
        print('Even')
    else:
        print('Odd')


# In[ ]:


myVar = 2.0
while myVar < 100:
    myVar = myVar * 1.65
else: 
    print(myVar)

