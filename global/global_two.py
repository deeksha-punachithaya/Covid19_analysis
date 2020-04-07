#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('covid_19_clean_complete.csv', parse_dates = ['Date'])
df.head(5)


# In[3]:


df.shape


# In[4]:


cases = ['Confirmed', 'Deaths', 'Recovered', 'Active']
df['Active'] = df['Confirmed'] - df['Recovered'] - df['Deaths']
df[cases] = df[cases].fillna(0)
df.sample(10)


# In[5]:


df[['Province/State']] = df[['Province/State']].fillna("")
df.sample()


# In[6]:


df['Country/Region'] = df['Country/Region'].replace('Mainland China', 'China')


# In[7]:


china = df[df['Country/Region'] == 'China']
not_china = df[df['Country/Region'] != 'China']
india = df[df['Country/Region'] == 'India']
india.sample(5)


# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(india.Date, india.Confirmed, color = 'g', label='Confirmed')
plt.plot(india.Date, india.Deaths, color = 'orange', label='Deaths')
plt.plot(india.Date, india.Recovered, color = 'red', label='Recovered')
plt.plot(india.Date, india.Active, color = 'blue', label='Active')
plt.legend()
plt.show()


# In[9]:


china = china.groupby('Date')[['Confirmed','Deaths','Recovered','Active']].sum().reset_index()


# In[10]:


plt.plot(india.Date, india.Active, 'r', label='India')
plt.plot(china.Date, china.Active, 'orange', label='China')
plt.legend()
plt.show()


# In[11]:


import pandas as pd 
from shapely.geometry import Point 
import geopandas as gpd
from mpl_toolkits.basemap import Basemap


# In[12]:


df.head()


# In[17]:


df1 = df.groupby(['Lat','Long'])['Confirmed'].max().reset_index()


# In[16]:


# import geopandas 

# world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

# world.head()


# In[21]:


from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(10,10))
m = Basemap(projection='mill')
m.drawcoastlines()
# m.etopo()

def plot_map(lat, lon):
    xpt, ypt = m(lon, lat)
    m.plot(xpt, ypt, 'o', markersize=5)
    return

df.apply(lambda x: plot_map(x['Lat'],x['Long']),axis=1)
plt.show()
# world.plot()
# geometry = [Point(xy) for xy in zip(df['Long'], df['Lat'])]
# crs = {'init': 'epsg:4326'}
# gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
# gdf.head()


# In[18]:


# gdf.plot(marker='.', color='b', markersize=0.005*df['Confirmed'])

