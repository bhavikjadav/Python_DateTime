#!/usr/bin/env python
# coding: utf-8

# # Find the gap of dates between 2 dates.

# In[1]:


import datetime


# In[2]:


tday = datetime.date(2020, 1, 1)


# In[7]:


dt1 = datetime.date(2019, 12, 1)


# In[9]:


print(f"The dates have the gap of {tday - dt1} days.")

