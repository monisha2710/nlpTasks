#!/usr/bin/env python
# coding: utf-8

# In[2]:


def gender_features(word):
    return {'last_letter':word[-1]}


# In[3]:


gender_features('nisha')


# In[4]:


from nltk.corpus import names


# In[5]:


labeled_names = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[7]:


print(labeled_names)


# In[8]:


import random


# In[9]:


random.shuffle(labeled_names)


# In[10]:


featuresets = [(gender_features(n),gender) for (n,gender) in labeled_names]


# In[11]:


print(featuresets)


# In[12]:


train_set,test_set = featuresets[500:],featuresets[:500]


# In[13]:


import nltk


# In[14]:


classifier = nltk.NaiveBayesClassifier.train(train_set)


# In[15]:


classifier.classify(gender_features('Monisha'))


# In[16]:


classifier.classify(gender_features('Pranjal'))


# In[17]:


print(nltk.classify.accuracy(classifier,test_set))


# In[ ]:




