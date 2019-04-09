#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import cmudict


# In[2]:


print(cmudict.entries()[653:659])


# In[3]:


from nltk.corpus import stopwords


# In[4]:


data = "This is some random text"


# In[5]:


stopwords=set(stopwords.words('english'))


# In[7]:


print(stopwords)


# In[14]:


from nltk.corpus import stopwords
print(stopwords.words('german'))


# In[ ]:




