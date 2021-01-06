#!/usr/bin/env python
# coding: utf-8

# # What will the next date after a week.

# In[1]:


import datetime


# In[4]:


tdelta = datetime.timedelta(days=7)


# In[5]:


tday = datetime.date.today()


# In[7]:


print(f"A Date after a week is {tday + tdelta}.")

