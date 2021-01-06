#!/usr/bin/env python
# coding: utf-8

# # Find that, How many days are there untill my birthday this year.

# In[1]:


import datetime


# In[10]:


bday = datetime.date(2021, 11, 18)


# In[11]:


tday = datetime.date.today()


# In[12]:


print(f"Remaining days : {bday - tday}.")

