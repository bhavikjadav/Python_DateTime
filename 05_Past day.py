#!/usr/bin/env python
# coding: utf-8

# # What was the date before 7 days.

# In[1]:


import datetime


# In[3]:


tday = datetime.date.today()


# In[4]:


tdelta = datetime.timedelta(days=7)


# In[5]:


print(f"Before 1 week the date was {tday - tdelta}.")

