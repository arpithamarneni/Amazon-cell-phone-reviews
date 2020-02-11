#!/usr/bin/env python
# coding: utf-8

# In[240]:


import pandas as pd
data= pd.read_csv("C:/Users/trinity/Downloads/Amazon Cell Phones Reviews.csv")
data.head()


# In[118]:


#Total different type of brands
data.groupby('brand').prices.count()


# In[157]:


data.isnull().count()


# In[120]:


data.info()


# In[121]:


data.columns.values


# In[159]:


from pandas import DataFrame
data["price1"]=data["prices"].dropna()


# In[154]:


data["prices"].dropna(inplace=True)


# In[243]:


data1=data[data["prices"].isna() == False]


# In[244]:


data1.head()


# In[173]:


data1.isnull().sum()


# In[174]:


data.info()


# In[204]:


data1.prices= data.prices.str.replace('$','')


# In[205]:


data1.head()


# In[181]:


data1.drop('price1', axis=1)


# In[184]:


data1.groupby('brand').prices.max()


# In[210]:


data2 = data1.loc[:,['brand','prices']]
data2.head()


# In[213]:


#the brand which has max price
data1[data1['prices'] == data1['prices'].max()].head()


# In[216]:


import matplotlib.pyplot as plt
plt.hist(data["rating"])


# In[219]:


#Average ratings of all brands
data1.groupby('brand').rating.mean()


# In[233]:


#brands with highest ratings
data1[data1['rating'] == data1['rating'].max()].title


# In[234]:


#Models which have least rating
data1[data1['rating'] == data1['rating'].min()].title


# In[246]:


new_data = pd.crosstab(data1.reviewUrl,data1.brand)
new_data.head()


# In[ ]:





# In[ ]:




