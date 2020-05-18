#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
get_ipython().run_line_magic('matplotlib', 'inline')
style.use('ggplot')
#Reading the meter data from the csv file
data=pd.read_csv(r'F:\Suman\fopassignment\Sample Usage File.csv',names=['Date and Time','Meter Reading'])
#filtering the data
date=pd.DataFrame(data['Date and Time'].str[1:10])
time=pd.DataFrame(data['Date and Time'].str[11:])
meterReading=pd.DataFrame(data['Meter Reading'])
date.columns=['Date']
time.columns=['Time']
meterReading.columns=['Meter Reading']
filtered=pd.DataFrame([date['Date'],time['Time'],meterReading['Meter Reading']])
filtered=filtered.transpose()
filtered['Units Consumed']=filtered['Meter Reading'].diff(1)
filtered['Units Consumed'].iloc[0]=0
#line diagram datewise
def lineplotDateWise():
    plt.plot(filtered['Date'],filtered['Units Consumed'],label="Unit Consumption",linewidth=5)
    plt.title('Unit Consumption as per the date')
    plt.xlabel('Date')
    plt.ylabel('Unit Consumption')
    plt.legend()
    plt.show()
def lineplotTimeWise():
        plt.plot(time['Time'],filtered['Units Consumed'],label="Unit Consumption",linewidth=5)
        plt.title('Unit Consumption as per the date')
        plt.xlabel('Time')
        plt.ylabel('Unit Consumption')
        plt.legend()
        plt.show()
def barDiagramDateWise():
    plt.bar(date['Date'],filtered['Units Consumed'],label='Units Consumed')
    plt.xlabel('Date')
    plt.ylabel('Units Consumed')
    plt.title('Units Consumed on particular date')
    plt.legend()
    plt.plot()
    plt.show()
def barDiagramTimeWise():
    plt.bar(time['Time'],filtered['Units Consumed'],label='Units Consumed')
    plt.xlabel('Time')
    plt.ylabel('Units Consumed')
    plt.title('Units Consumed on specific time')
    plt.legend()
    plt.plot()
    plt.show()
def histogram():
    plt.hist([filtered['Date'],filtered['Time'],filtered['Units Consumed']],bins=2)
    plt.show()


# In[46]:


lineplotDateWise()
lineplotTimeWise()
barDiagramDateWise()
barDiagramTimeWise()
histogram()


# In[ ]:





# In[ ]:




