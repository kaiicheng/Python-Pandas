#!/usr/bin/env python
# coding: utf-8

# In[35]:


## pandas 提供了新的資料結構


# In[36]:


# run in bash shell
get_ipython().system('pip install pandas')


# In[37]:


# run in python console
import pandas as pd


# In[39]:


movie_ratings = [8.0, 7.3, 8.5, 8.6]
ser = pd.Series(movie_ratings)


# In[40]:


# Pandas add index key.
print(type(ser))
print(ser)
print(ser[3])


# In[42]:


movie_titles = ['The Avengers', 'Avengers: Age of Ultron', 'Avengers: Infinite War', 'Avengers: Endgame']
ser = pd.Series(movie_ratings, index = movie_titles)
ser


# In[43]:


type(ser.values)


# In[46]:


print(ser.values)
print(ser.index)


# In[47]:


# Vectorization.
ser*10


# In[48]:


# Boolean type is applicable.
ser[ser >= 8]


# In[50]:


ser['Avengers: Infinite War']


# In[52]:


ser[2]


# In[ ]:





# In[ ]:





# In[ ]:





# In[57]:


avengers = pd.DataFrame()
avengers['movie'] = movie_titles
avengers['rating'] = movie_ratings
avengers


# In[58]:


type(avengers)


# In[59]:


avengers.index


# In[60]:


avengers.columns


# In[65]:


avengers['movie'].values


# In[68]:


avengers['movie'].values


# In[ ]:





# In[69]:


# Set is useful for joint, union and independent...
odds_index = pd.Index([1, 3, 5, 7, 9])
primes_index = pd.Index([2, 3, 5, 7])
print(odds_index & primes_index) # and
print(odds_index | primes_index) # or
print(odds_index ^ primes_index) # exclusive or


# In[70]:


# Joint
odds_index & primes_index


# In[71]:


odds_index | primes_index


# In[72]:


# XOR（Exclusive OR）
odds_index ^ primes_index


# In[ ]:


odds_index ^ primes_index


# In[73]:


odds_index.difference(primes_index)


# In[75]:


primes_index.difference(odds_index)


# In[ ]:


...


# In[ ]:





# In[ ]:





# In[76]:


movie_ratings = [9.0, 8.9, 8.8, 8.7]
ser = pd.Series(movie_ratings)
print(ser)


# In[ ]:





# In[ ]:





# In[ ]:





# In[77]:


movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
ser = pd.Series(movie_ratings, index=movie_titles)
print(ser.index)
print(ser.values)
print(ser)


# In[ ]:





# In[79]:


movie_dict = {
    "The Dark Knight": 9.0,
    "Schindler's List": 8.9,
    "Forrest Gump": 8.8,
    "Inception": 8.7
}
ser = pd.Series(movie_dict)
print(movie_dict.keys())
print(movie_dict.values())
print("\n")
print(ser.index)
print(ser.values)
print(ser)


# In[ ]:





# In[ ]:





# In[ ]:


# Read csv document


# In[82]:


df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/archived_data/archived_daily_case_updates/02-14-2020_1123.csv")
df


# In[ ]:





# In[84]:


# Read JSON file


# In[85]:


df = pd.read_json("https://python4ds.s3-ap-northeast-1.amazonaws.com/movies.json")
df


# In[ ]:





# In[ ]:


# Read data from database
# With SQL command


# In[83]:


import sqlite3

# Creating a demo.db database in working directory
conn = sqlite3.connect('demo.db')
# Importing a table
movie_ratings = [9.0, 8.9, 8.8, 8.7]
movie_titles = ["The Dark Knight", "Schindler's List", "Forrest Gump", "Inception"]
df = pd.DataFrame()
df["title"] = movie_titles
df["rating"] = movie_ratings
df.to_sql("movies", index=False, con=conn, if_exists='replace')
# Importing data from demo.movies
query_str = """
SELECT *
    FROM movies
    WHERE rating < 9.0;
"""
pd.read_sql(query_str, con=conn)

