#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk.corpus


# In[2]:


# The Brown corpus:


# In[4]:


print(str(nltk.corpus.brown).replace('\\\\','/'))


# In[5]:


from nltk.corpus import brown


# In[6]:


print(brown.words())


# In[7]:


print(brown.tagged_words())


# In[8]:


print(brown.sents())


# In[9]:


print(brown.tagged_sents())


# In[10]:


print(brown.categories())


# In[11]:


print(brown.words(categories='news'))


# In[8]:


print(brown.sents(categories=['news', 'editorial', 'reviews']))


# In[7]:


brown.sents(categories=['news', 'editorial', 'reviews'])


# In[3]:


from nltk.corpus import brown


# In[5]:


print(brown.sents(categories=['news', 'editorial', 'reviews']))


# In[6]:


print(brown.sents(categories=['hobbies', 'editorial', 'reviews']))


# In[ ]:




