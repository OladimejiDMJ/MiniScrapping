#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import selenium
from selenium import webdriver
#import pandas 
import pandas as pd
#i will be using Chrome webdriver
#Create a the driver object
driver=webdriver.Chrome(r'C:\Users\user\Desktop\chromedriver_win32\chromedriver')
#use the driver object to open the webpage that contain our data
driver.get('https://www.biopharmcatalyst.com/calendars/historical-catalyst-calendar')
#the information we need are Ticker,Drug,Stage,Note, and Date. We will find the element by class name.There are other ways to locate the elements but this is simpler
Ticker=driver.find_elements_by_class_name('ticker')
Drug=driver.find_elements_by_class_name('drug')
Stage=driver.find_elements_by_class_name('stage')
Note = driver.find_elements_by_class_name("catalyst-note")
Date = driver.find_elements_by_class_name("catalyst-date")
#Create empty list for each of the object created above
list_Ticker=[]
list_Drug=[]
list_Stage=[]
list_Note=[]
list_Date=[]
#append each of the lists
for d in Drug:
    list_Drug.append(d.text)
for s in Stage:
    list_Stage.append(s.text)
for n in Note:
    list_Note.append(n.text)
for t in Ticker:
    list_Ticker.append(t.text)
for da in Date:
    list_Date.append(da.text)
#Create a panda dataframe
df=pd.DataFrame({'TICKER':list_Ticker,'Stage':list_Stage,'Catalyst_Note':list_Note,'Drug':list_Drug,'Date':list_Date})
#Create an excel writer where we can store our new scrapped data
writer=pd.ExcelWriter('pandas_simple.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name="Sheet1")
writer.save()

