#!/usr/bin/env python
# coding: utf-8

# In[6]:


#The Null Hypothesis H0 is "Has the Apparent temperature and humidity compared monthly
#across 10 years of the data indicate an increase due to Global warming"


# In[2]:


#Importing libraries
import numpy as np 
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#Loaing data
df=pd.read_csv("weatherHistory.csv")


# In[50]:


df.head()


# In[51]:


df.dtypes


# In[52]:


df["Formatted Date"]


# In[53]:



df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df['Formatted Date']


# In[54]:


#convert object to date time
df.dtypes


# In[55]:


df = df.set_index('Formatted Date')
df.head()


# In[56]:


#Resampling hour to month
data_columns = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df[data_columns].resample('MS').mean()
df_monthly_mean.head()


# In[63]:


#Plotting graph

plt.title("Variation in Apparent Temperature and Humidity with time")
plt.figure(figsize=(14,6))
sns.lineplot(data=df_monthly_mean)


# In[58]:


#retrieving the data of a particular month from every year, say April
#df1 = df_monthly_mean[df_monthly_mean.index.month==4]
#print(df1)
#df1.dtypes
#df1.head()


# In[70]:


#import matplotlib.dates as mdates
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %Y'))
plt.figure(figsize=(15,6))
plt.title("Variation in Apparent Temperature and Humidity with time")
#sns.lineplot(data=df_monthly_mean)
plt.xlabel("Month of April")
plt.plot(df1)


# # Conclusion

# # No change in average humidity over the ten years from 2006 to 2016. Increase in average apparent temperature can be seen in the year 2009 then again it dropped in 2010 ,then a slight increase in 2011 then a significant drop is observed in 2015 and again it increased in 2016.

# In[ ]:




