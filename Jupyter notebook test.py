#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
import sympy as sp
from matplotlib import *
import matplotlib as plt

t = sp.Symbol('t')

x = sp.Function('x')(t)

y = sp.Function('y')(t)


eq = Eq(x.diff(t)+x,0)

display(eq)

f = dsolve(eq,x)

display(f)


# In[ ]:




