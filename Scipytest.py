#!/usr/bin/env python
# coding: utf-8

# In[31]:


from scipy.integrate import solve_ivp
from numpy import *
import numpy as np
from matplotlib import pyplot as plt

#First example A circle

def f(t, r): #function to solve variables are backwards
    x,y = r
    fx = np.cos(y)
    fy = np.sin(x)
    return fx, fy

sol = solve_ivp( f,(0,10),(1,1), t_eval=np.linspace(0, 10, 100))# t_eval will help later in ploting now solve ivp will find 100 points between 0 and 10 change values here to change what is plotted

x, y = sol.y
t = sol.t
plt.plot(x, y)
plt.axis("scaled")
plt.show()
plt.plot(t, x)
plt.axis("scaled")
plt.show()


# 

# In[65]:


from scipy.integrate import solve_ivp
from numpy import *
import numpy as np
from matplotlib import pyplot as plt

def f(x, y):
    fy = (y**2)*(1+x)
    return fy

sol = solve_ivp( f,(1,10),(1,2), t_eval=np.linspace(1, 10, 100))# for middle y(1)=2

y = sol.y
plt.plot(y)
#plt.axis("scaled")
plt.show()


# In[ ]:




