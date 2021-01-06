#!/usr/bin/env python
# coding: utf-8

# # Use pytz

# In[1]:


import datetime
import pytz


# In[2]:


dt = datetime.datetime(2020, 1, 7, 4, 48, 50, tzinfo=pytz.UTC)


# In[3]:


print(dt)

