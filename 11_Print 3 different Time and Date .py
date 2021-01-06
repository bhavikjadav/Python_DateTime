#!/usr/bin/env python
# coding: utf-8

# # Tip : You can use now(), utcnow(), today()

# In[1]:


import datetime


# In[2]:


dt_today = datetime.datetime.today()


# In[3]:


dt_now = datetime.datetime.now()


# In[4]:


dt_utcnow = datetime.datetime.utcnow()


# In[5]:


print(dt_today)
print(dt_now)
print(dt_utcnow)

