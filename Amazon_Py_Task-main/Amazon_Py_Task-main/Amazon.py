#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


# In[2]:


import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


# In[13]:


driverPath = r"C:\Users\Merit.MSSPLACA002\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get("https://www.amazon.in/s?k=pendrives+offers+combo&crid=1SG8247AYLAEN&sprefix=pendrives+offers%2Cfashion%2C280&ref=nb_sb_ss_fb_1_16_ts-doa-p")

driver.maximize_window()

#------------------------------------PRODUCT_NAME----------

a = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

l=[]
for i in a:
    if i.text != '':
        l.append(i.text.split("\n"))
print(l, end=" ")

#-------------------------------------NEW_PRICE----------
b = driver.find_elements_by_xpath("//span[@class='a-price-whole']")

l1=[]
for j in b:
    
        l1.append(j.text.split("\n"))
print(l1, end=" ")

#------------------------------------OLD_PRICE----------
c = driver.find_elements_by_xpath("//span[@class='a-price a-text-price']")

l2=[]
for h in c:
   
        l2.append(h.text.split("\n"))
print(l2, end=" ")

writer =pd.ExcelWriter('AMAZONS3_PENDRIVES.xlsx', engine ='xlsxwriter')

df=pd.DataFrame(list(zip(l,l1,l2)),columns=["PRODUCT_NAME","NEW_PRICE","OLD PRICE"])



df.to_excel(writer,sheet_name='PRODUCT_PRICE', index = False )

writer.save()
writer.close()


# In[ ]:




