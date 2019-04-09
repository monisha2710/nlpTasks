#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import TweetTokenizer


# In[2]:


tknzr = TweetTokenizer()


# In[3]:


s1 = '@remy: This is waaaaayyyy too much for you!!!!!!'


# In[5]:


tknzr.tokenize(s1)


# In[ ]:




