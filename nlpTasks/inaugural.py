#!/usr/bin/env python
# coding: utf-8

# In[4]:


from nltk.corpus import inaugural


# In[5]:


inaugural.words('1789-Washington.txt')


# In[6]:


inaugural.raw('1789-Washington.txt')


# In[7]:


inaugural.sents('1789-Washington.txt')


# In[8]:


inaugural.paras('1789-Washington.txt')


# In[1]:


from nltk.corpus import wordnet as wn
wn.synsets('dog')


# In[ ]:




