#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


request_url = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
html_tables = pd.read_html(request_url)
olympic_medal_table = html_tables[1]
column_names = ['team', 'no_summer_games', 'no_summer_golds', 'no_summer_silvers', 'no_summer_bronzes', 'no_summer_totals',
               'no_winter_games', 'no_winter_golds', 'no_winter_silvers', 'no_winter_bronzes', 'no_winter_totals',
               'no_combined_games', 'no_combined_golds', 'no_combined_silvers', 'no_combined_bronzes', 'no_combined_totals']
olympic_medal_table.columns = column_names
team_name_split = olympic_medal_table['team'].str.split('\(|\)|\[|\]', expand=True)
team_names = team_name_split[0].str.strip()
team_ioc = team_name_split[1].str.strip()
olympic_medal_table.insert(0, 'team_name', team_names.values)
olympic_medal_table.insert(1, 'team_ioc', team_ioc.values)
olympic_medal_table = olympic_medal_table.drop('team', axis=1)


# In[5]:


olympic_medal_table.shape


# In[6]:


olympic_medal_table.head()


# In[31]:


olympic_medal_table.tail()


# In[86]:


olympic_medal_table


# In[ ]:





# In[7]:


## 隨堂練習：哪個國家贏得的夏季奧運金牌數最多？


# In[206]:


def most_summer_gold_country(olympic_medal_table):
    """
    >>> most_summer_gold_country(olympic_medal_table)
    'United States'
    """
    
    # (i)
    without_totals = olympic_medal_table[olympic_medal_table['team_name'] != 'Totals']
    without_totals = without_totals.set_index('team_name')
    return without_totals["no_summer_golds"].idxmax()
    
    
    # (ii)
#     without_totals = olympic_medal_table[olympic_medal_table['team_name'] != 'Totals']
#     n_largest = without_totals['no_summer_golds'].max()
#     id_largest = without_totals['no_summer_golds'].idxmax()
#     print(id_largest)
#     print(without_totals.loc[140, 'team_name'])
#     team_largest= without_totals.loc[without_totals['no_summer_golds'].idxmax(), 'team_name']
#     print(team_largest)
#     return(team_largest)


# In[207]:


most_summer_gold_country(olympic_medal_table)


# In[ ]:





# In[99]:


## 隨堂練習：哪個國家夏季奧運與冬季奧運的金牌數差距數最大？


# In[217]:


def largest_gold_difference(olympic_medal_table):
    """
    >>> largest_gold_difference(olympic_medal_table)
    'United States'
    """
    
    # (i)
    without_totals = olympic_medal_table.loc[:151,]   # 151 included.
    without_totals = without_totals.set_index("team_name")   # Set "team_name" as index.
    diff = without_totals["no_summer_golds"] - without_totals["no_winter_golds"]
    return diff.idxmax()
    
    
    # (ii)
#     without_totals = olympic_medal_table[olympic_medal_table['team_name'] != 'Totals']
#     without_totals["largest_difference"] = without_totals["no_summer_golds"] - without_totals ["no_winter_golds"]
#     team_largest_diff= without_totals.loc[without_totals['largest_difference'].idxmax(), 'team_name']
#     print(team_largest_diff)
#     return team_largest_diff

    


# In[218]:


largest_gold_difference(olympic_medal_table)


# In[ ]:





# In[10]:


## 隨堂練習：哪個國家夏季奧運與冬季奧運的金牌數差距除以總金牌數的比例最大？（僅考慮至少有一個夏季金牌與一個冬季金牌的國家）


# In[230]:


def largest_ratio(olympic_medal_table):
    """
    >>> largest_ratio(olympic_medal_table)
    'Hungary'
    """
    # (i)
    without_totals = olympic_medal_table.loc[:151,]   # 151 included.
    without_totals = without_totals.set_index("team_name")   # Set "team_name" as index.
    numerator = without_totals["no_summer_golds"] - without_totals["no_winter_golds"]
    denominator = without_totals["no_summer_golds"] + without_totals["no_winter_golds"]
    ratio = numerator/denominator
    
    # Create a new series to store data with ratio isn't 1.
    ratio__is_not_one = ratio[ratio!=1]
    # print(type(ratio__is_not_one))
    return ratio__is_not_one.idxmax()
    
    
    
    
    # (ii)
#     without_totals = olympic_medal_table[olympic_medal_table['team_name'] != 'Totals']
#     without_totals = without_totals [(without_totals["no_summer_golds"] > 0) & (without_totals["no_winter_golds"] > 0)]
    
#     without_totals["largest_ratio"] = (without_totals["no_summer_golds"] - without_totals ["no_winter_golds"])/ (without_totals["no_summer_golds"] + without_totals ["no_winter_golds"])

#     team_largest_ratio= without_totals.loc[without_totals['largest_ratio'].idxmax(), 'team_name']
#     print(team_largest_ratio)
#     return team_largest_ratio


# In[231]:


largest_ratio(olympic_medal_table)


# In[232]:


olympic_medal_table[olympic_medal_table['team_name'] == 'Hungary']


# In[ ]:


# Performance of Hungary in Summer Olympics is much better than one in Winter.

