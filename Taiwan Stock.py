#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[3]:


def get_price_rank():
    query_str_parameters = {
        't': 'pri',
        'e': 'tse',
        'n': '100'
    }
    request_url = "https://tw.stock.yahoo.com/d/i/rank.php"
    response = requests.get(request_url, params=query_str_parameters)
    soup = BeautifulSoup(response.text)
    stock_tickers = []
    stock_names = []
    for e in soup.select(".name a"):
        stock_ticker = e.text.split()[0]
        stock_name = e.text.split()[1]
        stock_tickers.append(stock_ticker)
        stock_names.append(stock_name)
    prices = [float(e.text) for e in soup.select('.name+ td')]
    return stock_tickers, stock_names, prices


# In[4]:


stock_tickers, stock_names, prices = get_price_rank()


# In[5]:


print(stock_tickers)
print(stock_names)
print(prices)


# In[8]:


from statistics import median

ky_prices = [price for stock_name, price in zip(stock_names, prices) if "KY" in stock_name]
median(ky_prices)


# In[11]:


# 17 of 100 companies are high prices stock with "KY" sign.
ky_prices = list()
for n, p in zip(stock_names, prices):
    if 'KY' in n:
        ky_prices.append(p)
print(len(ky_prices))


# In[12]:


ky_prices


# In[ ]:





# In[ ]:





# In[ ]:





# In[13]:


## Python 一直以來都非常適合資料處理，但她的分析能力很薄弱，`pandas` 的開發有助於補足 Python 資料分析的需求，讓使用者能夠在 Python 中執行完整的資料分析流程，而無需切換到 data-centric 的特定語言，如 R。


# In[17]:


import pandas as pd

df = pd.DataFrame()
df["ticker"] = stock_tickers
df["name"] = stock_names
df["price"] = prices
df.head()


# In[18]:


df.tail()


# In[19]:


df['price']


# In[20]:


df['name']


# In[21]:


# Get data of a single company.
df.dtypes


# In[22]:


df.loc[0, :]


# In[23]:


df.loc[0, ]


# In[24]:


# Get data of companies with "KY" sign.
df[df["name"].str.contains('KY')]


# In[26]:


df[df["name"].str.contains('KY')]['price']


# In[28]:


df[df["name"].str.contains("KY")]["price"].median()


# In[ ]:





# In[ ]:





# In[ ]:





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


# In[ ]:




