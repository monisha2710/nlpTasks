#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# In[4]:


stemmer = PorterStemmer()
example = """Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.[1] Data mining is an interdisciplinary subfield of computer science and statistics with an overall goal to extract information (with intelligent methods) from a data set and transform the information into a comprehensible structure for further use.[1][2][3][4] Data mining is the analysis step of the "knowledge discovery in databases" process, or KDD.[5] Aside from the raw analysis step, it also involves database and data management aspects, data pre-processing, model and inference considerations, interestingness metrics, complexity considerations, post-processing of discovered structures, visualization, and online updating.[1] The difference between data analysis and data mining is that data analysis is to summarize the history such as analyzing the effectiveness of a marketing campaign, in contrast, data mining focuses on using specific machine learning and statistical models to predict the future and discover the patterns among data"""
example = [stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))
#Do it for file


# In[8]:


lemmatizer = WordNetLemmatizer()
example = "A cat was chasing the mice. There was cacti around the corner"
example = [lemmatizer.lemmatize(token) for token in example.split(" ")]
print(" ".join(example))


# In[13]:


#Stemming a file
stemmer = PorterStemmer()
f = open("Desktop/test1.txt","r")
example = f.read()
example = [stemmer.stem(token) for token in example.split(" ")]
print(" ".join(example))


# In[2]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[18]:


vect = CountVectorizer(binary = True)
corpus = ["""Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems""",""""Data mining is an interdisciplinary subfield of computer science and statistics with an overall goal to extract information (with intelligent methods) from a data set and transform the information into a comprehensible structure for further use.""",""" Data mining is the analysis step of the "knowledge discovery in databases" process, or KDD""","""Aside from the raw analysis step, it also involves database and data management aspects, data pre-processing, model and inference considerations, interestingness metrics, complexity considerations, post-processing of discovered structures, visualization, and online updating"""]
vect.fit(corpus)
print(vect.transform(["Data mining"]).toarray())


# In[21]:


vect = TfidfVectorizer(binary = False)
corpus = ["""Data mining is the process of discovering patterns""",""""Data mining is an interdisciplinary subfield of computer science and statistics """,""" Data mining is the analysis step of the knowledge discovery in databases process"""]
vect.fit(corpus)
print(vect.transform(["Data mining"]).toarray())


# In[22]:


from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["""Data mining is the process of discovering patterns""",""""Data mining is an interdisciplinary subfield of computer science""",""" Data mining is the analysis step of the knowledge discovery in databases process"""]
))
print(similarity)


# In[8]:


from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer(binary = False)
corpus = ["""If there is a phrase I would prefer to retire from online bios, personal or professional, it is, "I love travel". Or some approximation of that sentiment. To clarify, I am not against travellers or those who proudly flaunt their passion for travel. On the contrary, editing a travel magazine has now made me oddly protective of travellers and their ilk. My submission is that "love to travel" , suggested so casually, just doesnt feel adequate to the depth of emotion it sparks in true devotees.""","""One of the finer books I read this year was John Kaag's Hiking With Nietzsche, in which Kaag, a professor of philosophy, rekindles his passion for the German thinker while tracing picturesque hiking trails in the mountains of Switzerland. It's a near-precise rendering of the travelogue as a self-help book. A young Kaag was an avowed Nietzsche acolyte but given the ravages of responsibilities and adulthood, the writer put affinity to test by undertaking physically enduring hikes through the Alps, revisiting haunts that the philosopher escaped to, in search of solitude and salve. The journey's demands, coupled with his own inner turmoil, are catnip for anybody feeling at cross purposes with their own life."""]
vect.fit(corpus)
print(vect.transform(corpus).toarray())
print
print

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform(["""If there is a phrase I would prefer to retire from online bios, personal or professional, it is, "I love travel". Or some approximation of that sentiment. To clarify, I am not against travellers or those who proudly flaunt their passion for travel. On the contrary, editing a travel magazine has now made me oddly protective of travellers and their ilk. My submission is that "love to travel" , suggested so casually, just doesnt feel adequate to the depth of emotion it sparks in true devotees.
""",""""One of the finer books I read this year was John Kaag's Hiking With Nietzsche, in which Kaag, a professor of philosophy, rekindles his passion for the German thinker while tracing picturesque hiking trails in the mountains of Switzerland. It's a near-precise rendering of the travelogue as a self-help book. A young Kaag was an avowed Nietzsche acolyte but given the ravages of responsibilities and adulthood, the writer put affinity to test by undertaking physically enduring hikes through the Alps, revisiting haunts that the philosopher escaped to, in search of solitude and salve. The journey's demands, coupled with his own inner turmoil, are catnip for anybody feeling at cross purposes with their own life."""]
))
#print(similarity)


# In[18]:


#Cosine Similarity of 2 articles

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer
#vect = CountVectorizer(binary = True)

vect = TfidfVectorizer(binary = False)
f = open("Desktop/d1.txt","r")
c1 = f.read()
f.close()
f = open("Desktop/d2.txt","r")
c2 = f.read()
f.close()
corpus = [c1 , c2]
vect.fit(corpus)

print(vect.transform(corpus).toarray())
print
print

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vect.transform([c1,c2]
))
print("Similarity:")
print(similarity)


# In[ ]:




