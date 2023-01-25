#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from apyori import apriori
import networkx as nx
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_excel('orphan-entity-allocation\AssociationMining\Minningdata.xlsx')
data.head()

def search(value):
    terms = []
    for index, row in data.iterrows():
        if row['Source'] == value:
            terms.append(row['Target'])
        else:
            pass
    return terms
            
# output1 = search('Aerospace Engineering')
# print(output1)

# print("\n")

# output2 = search('Web Developer')
# print(output2)

# print("\n")

# output3 = search('Financial Services')
# print(output3)


# # In[ ]:




