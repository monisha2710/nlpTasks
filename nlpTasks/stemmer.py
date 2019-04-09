#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.stem import PorterStemmer


# In[3]:


stemmerporter=PorterStemmer()


# In[4]:


stemmerporter.stem('running')


# In[5]:


stemmerporter.stem('happiness')


# In[6]:


stemmerporter.stem('gaming')


# In[7]:


stemmerporter.stem('coding')


# In[8]:


stemmerporter.stem('cooking')


# In[9]:


stemmerporter.stem('worrying')


# In[10]:


stemmerporter.stem('singer')


# In[11]:


stemmerporter.stem('Dying')


# In[12]:


stemmerporter.stem('dying')


# In[13]:


stemmerporter.stem('Worrying')


# In[15]:


stemmerporter.stem('sadden')


# In[16]:


stemmerporter.stem('saddening')


# In[17]:


from nltk.stem import LancasterStemmer


# In[18]:


stemmerLan = LancasterStemmer()


# In[19]:


stemmerLan.stem('worrying')


# In[20]:


stemmerLan.stem('sadden')


# In[21]:


stemmerLan.stem('saddening')


# In[22]:


stemmerLan.stem('worthless')


# In[23]:


stemmerLan.stem('worthy')


# In[24]:


stemmerporter.stem('worthless')


# In[25]:


stemmerLan.stem('worthy')


# In[26]:


stemmerporter.stem('happen')


# In[27]:


stemmerLan.stem('happen')


# In[28]:


stemmerLan.stem('happened')


# In[29]:


stemmerporter.stem('happened')


# In[30]:


stemmerporter.stem('ruiner')


# In[31]:


stemmerLan.stem('ruiner')


# In[32]:


stemmerporter.stem('singer')


# In[33]:


stemmerLan.stem('singer')


# In[34]:


stemmerporter.stem('disable')


# In[35]:


stemmerLan.stem('disable')


# In[36]:


stemmerporter.stem('uncomfortable')


# In[38]:


stemmerLan.stem('uncomfortable')


# In[39]:


stemmerLan.stem('discomforting')


# In[40]:


stemmerLan.stem('discomfort')


# In[41]:


from nltk.stem import SnowballStemmer


# In[43]:


stemmerSno = SnowballStemmer('german')


# stemmerSno.stem('laufen')

# In[45]:


stemmerLan.stem('paralysis')


# In[46]:


stemmerporter.stem('paralysis')


# In[ ]:




