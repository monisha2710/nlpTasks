#!/usr/bin/env python
# coding: utf-8

# In[1]:


texts = [
    """
    Babylon was a significant city in ancient Mesopotamia,
    in the fertile plain between the Tigris and Euphrates rivers.
    The city was built upon the Euphrates, and divided in equal parts along its left and right banks,
    with steep embankments to contain the river's seasonal floods.
    """,
    """
    Hammurabi was the sixth Amorite king of Babylon
    from 1792 BC to 1750 BC middle chronology.
    He became the first king of the Babylonian Empire following the abdication of his father,
    Sin-Muballit, who had become very ill and died, extending Babylon's control over Mesopotamia
    by winning a series of wars against neighboring kingdoms.
    """
]
 


# In[2]:


def source(texts, targets):
    for text in texts:
        for t in targets:
            t.send(text)
 


# In[ ]:


@coroutine
def sent_tokenize_pipeline(targets):
    while True:
        text = (yield)
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            for target in targets:
                target.send(sentence)
 
@coroutine
def word_tokenize_pipeline(targets):
    while True:
        sentence = (yield)
        words = nltk.word_tokenize(sentence)
        for target in targets:
            target.send(words)
 
@coroutine
def pos_tag_pipeline(targets):
    while True:
        words = (yield)
        tagged_words = nltk.pos_tag(words)
 
        for target in targets:
            target.send(tagged_words)
 
@coroutine
def ne_chunk_pipeline(targets):
    while True:
        tagged_words = (yield)
        ner_tagged = nltk.ne_chunk(tagged_words)
 
        for target in targets:
            target.send(ner_tagged)
 

