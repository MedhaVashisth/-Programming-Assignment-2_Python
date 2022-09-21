#!/usr/bin/env python
# coding: utf-8

# In[1]:


kilometers = float(input("Enter value in kilometers: "))


# In[2]:


conv_fac = 0.621371


# In[3]:


miles = kilometers * conv_fac


# In[4]:


print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[5]:


celsius = 37.5


# In[6]:


fahrenheit = (celsius * 1.8) + 32


# In[7]:


print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[8]:


import calendar


# In[9]:


yy = 2014  # year
mm = 11    # month


# In[10]:


yy = int(input("Enter year: "))
mm = int(input("Enter month: "))


# In[11]:


print(calendar.month(yy, mm))


# In[13]:


import cmath


# In[14]:


a = 1
b = 5
c = 6


# In[15]:


d = (b**2) - (4*a*c)


# In[16]:


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)


# In[17]:


print('The solution are {0} and {1}'.format(sol1,sol2))


# In[18]:


# Python code to swap two numbers
# without using another variable


x = 5
y = 7

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'
x, y = y, x

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:




