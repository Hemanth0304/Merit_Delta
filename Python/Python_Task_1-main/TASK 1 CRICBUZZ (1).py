#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


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


# In[36]:


driverPath = r"C:\Users\Merit.MSSPLACA002\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting")

driver.maximize_window()

 #-------------------------------------------------BATTING------------------------------------------------------------
    
driver.find_element_by_xpath("//a[@id='batsmen-tests-tab']").click()

                             
a = driver.find_elements_by_xpath("//a[@id='batsmen-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l=[]
for i in a:
    if i.text != '':
        l.append(i.text.split("\n"))
print(l, end=" ")

#-------------------------------------------------
driver.find_element_by_xpath("//a[@id='batsmen-odis-tab']").click()
b=driver.find_elements_by_xpath("//a[@id='batsmen-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l1=[]
for j in b:
    if j.text != '':
        l1.append(j.text.split("\n"))
print(l1, end=" ")


#------------------------------------------------- 

driver.find_element_by_xpath("//a[@id='batsmen-t20s-tab']").click()
c =driver.find_elements_by_xpath("//a[@id='batsmen-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l2=[]
for h in c:
    if h.text != '':
        l2.append(h.text.split("\n"))
print(l2, end=" ")


writer =pd.ExcelWriter('CRICBUZZ.xlsx', engine ='xlsxwriter')

df=pd.DataFrame(l,columns=["position", "POW", "PROFILE", "player", "Rating"])
df.drop('POW', axis=1, inplace=True)

df.to_excel(writer,sheet_name='test', index = False )




df2=pd.DataFrame(l1,columns=["position", "POW", "PROFILE", "player", "Rating"])
df2.drop('POW', axis=1, inplace=True)

df2.to_excel(writer,sheet_name='ODI', index = False )


df3=pd.DataFrame(l2,columns=["position", "POW", "PROFILE", "player", "Rating"])
df3.drop('POW', axis=1, inplace=True)

df3.to_excel(writer,sheet_name='T20s', index = False )

writer.save()


writer.close()


#---------------------------------------------------BOWLING------------------------------------------------------------------------

#BOWLING-----TEST-----

driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()

Bowling_Test = driver.find_elements_by_xpath("//a[@id='bowlers-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l3=[]
for h in Bowling_Test:
    if h.text != '':
        l3.append(h.text.split("\n"))
print(l3, end=" ")

#BOWLING-----ODI-----


driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()

Bowling_ODI = driver.find_elements_by_xpath("//a[@id='bowlers-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")



l4=[]

for B2 in Bowling_ODI:
    if B2.text != '':
        l4.append(B2.text.split("\n"))
print(l4, end=" ")

#BOWLING-----T20s-----

driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()

Bowling_T20s = driver.find_elements_by_xpath("//a[@id='bowlers-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")



l5=[]

for B3 in Bowling_T20s:
    if B3.text != '':
        l5.append(B3.text.split("\n"))
print(l5, end=" ")






writer =pd.ExcelWriter('BOWLERS.xlsx', engine ='xlsxwriter')


Bowling_Test_01=pd.DataFrame(l3,columns=["position", "POW", "PROFILE", "player", "Rating"])
Bowling_Test_01.drop('POW', axis=1, inplace=True)

Bowling_Test_01.to_excel(writer,sheet_name='test', index = False )

#--------------

Bowling_ODI_02=pd.DataFrame(l4,columns=["position", "POW", "PROFILE", "player", "Rating"])
Bowling_ODI_02.drop('POW', axis=1, inplace=True)

Bowling_ODI_02.to_excel(writer,sheet_name='ODI', index = False )

#-------------
Bowling_T20s_03=pd.DataFrame(l5,columns=["position", "POW", "PROFILE", "player", "Rating"])
Bowling_T20s_03.drop('POW', axis=1, inplace=True)

Bowling_T20s_03.to_excel(writer,sheet_name='T20s', index = False )


writer.save()


writer.close()


#---------------------------------------------------ALL ROUNDERS-----------------------------------------------------------------------

driver.find_element_by_xpath("//a[@id='all-rounders-tab']").click()

                             
allrounders = driver.find_elements_by_xpath("//a[@id='allrounders-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l6=[]
for al in allrounders:
    if al.text != '':
        l6.append(al.text.split("\n"))
print(l6, end=" ")

#-------------------------------------------------
driver.find_element_by_xpath("//a[@id='all-rounders-tab']").click()

aodi =driver.find_elements_by_xpath("//a[@id='allrounders-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l7=[]
for alo in aodi:
    if alo.text != '':
        l7.append(alo.text.split("\n"))
print(l7, end=" ")


#------------------------------------------------- 

driver.find_element_by_xpath("//a[@id='all-rounders-tab']").click()

at =driver.find_elements_by_xpath("//a[@id='allrounders-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l8=[]
for at20 in at:
    if at20.text != '':
        l8.append(at20.text.split("\n"))
print(l8, end=" ")


writer =pd.ExcelWriter('ALLROUNDERS.xlsx', engine ='xlsxwriter')

df30=pd.DataFrame(l6,columns=["position", "POW", "PROFILE", "player", "Rating"])
df30.drop('POW', axis=1, inplace=True)

df30.to_excel(writer,sheet_name='test', index = False )




df31=pd.DataFrame(l7,columns=["position", "POW", "PROFILE", "player", "Rating"])
df31.drop('POW', axis=1, inplace=True)

df31.to_excel(writer,sheet_name='ODI', index = False )


df33=pd.DataFrame(l8,columns=["position", "POW", "PROFILE", "player", "Rating"])
df33.drop('POW', axis=1, inplace=True)

df33.to_excel(writer,sheet_name='T20s', index = False )




#---------------------------------------------------TEAMS-----------------------------------------------------------------------

driver.find_element_by_xpath("//a[@id='teams-tests-tab']").click()

                             
aa = driver.find_elements_by_xpath("//a[@id='teams-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center')]")

la=[]
for ia in aa:
    if ia.text != '':
        la.append(ia.text.split("\n"))
print(la, end=" ")



driver.find_element_by_xpath("//a[@id='teams-tests-tab']").click()
ba= driver.find_elements_by_xpath("//a[@id='teams-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center')]")

l2a=[]
for ja in ba:
    if ja.text != '':
        l2a.append(ja.text.split("\n"))
print(l2a, end=" ")




driver.find_element_by_xpath("//a[@id='teams-tests-tab']").click()

ca = driver.find_elements_by_xpath("//a[@id='teams-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center')]")

l3a=[]
for ka in ca:
    if ka.text != '':
        l3a.append(ka.text.split("\n"))
print(l3a, end=" ")


writer =pd.ExcelWriter('TEAMSS.xlsx', engine ='xlsxwriter')

df=pd.DataFrame(la,columns=["position",  "PROFILE", "player", "Rating"])

df.to_excel(writer,sheet_name='test', index = False )

writer.close()


df1=pd.DataFrame(l2a,columns=["position",  "PROFILE", "player", "Rating"])

df1.to_excel(writer,sheet_name='odi', index = False )



df1=pd.DataFrame(l3a,columns=["position",  "PROFILE", "player", "Rating"])

df1.to_excel(writer,sheet_name='T20', index = False )

writer.save()


writer.close()


driver.close()


# In[9]:


driverPath = r"C:\Users\Merit.MSSPLACA002\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/all-rounder")

driver.maximize_window()

driver.find_element_by_xpath("//a[@id='allrounders-tests-tab']").click()

                             
a = driver.find_elements_by_xpath("//a[@id='allrounders-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l=[]
for i in a:
    if i.text != '':
        l.append(i.text.split("\n"))
print(l, end=" ")



driver.find_element_by_xpath("//a[@id='allrounders-odis-tab']").click()
b=driver.find_elements_by_xpath("//a[@id='allrounders-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l2=[]
for j in b:
    if j.text != '':
        l2.append(j.text.split("\n"))
print(l2, end=" ")




driver.find_element_by_xpath("//a[@id='allrounders-t20s-tab']").click()
c=driver.find_elements_by_xpath("//a[@id='allrounders-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l3=[]
for k in c:
    if k.text != '':
        l3.append(k.text.split("\n"))
print(l3, end=" ")


writer =pd.ExcelWriter('Allroundersss.xlsx', engine ='xlsxwriter')

df=pd.DataFrame(l,columns=["position", "POW", "PROFILE", "player", "Rating"])
df.drop('POW',axis=1,inplace=True)
df.to_excel(writer,sheet_name='test', index = False )




df1=pd.DataFrame(l2,columns=["position", "POW", "PROFILE", "player", "Rating"])
df1.drop('POW',axis=1,inplace=True)
df1.to_excel(writer,sheet_name='odi', index = False )



df1=pd.DataFrame(l3,columns=["position", "POW", "PROFILE", "player", "Rating"])
df1.drop('POW',axis=1,inplace=True)
df1.to_excel(writer,sheet_name='T20', index = False )
writer.save()


writer.close()
driver.close()


# In[8]:


#bowling

driverPath = r"C:\Users\Merit.MSSPLACA002\Desktop\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get("https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling")

driver.maximize_window()

driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()

                             
a = driver.find_elements_by_xpath("//a[@id='bowlers-tests-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l=[]
for i in a:
    if i.text != '':
        l.append(i.text.split("\n"))
print(l, end=" ")



driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()
b=driver.find_elements_by_xpath("//a[@id='bowlers-odis-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l2=[]
for j in b:
    if j.text != '':
        l2.append(j.text.split("\n"))
print(l2, end=" ")




driver.find_element_by_xpath("//a[@id='bowlers-tab']").click()
c=driver.find_elements_by_xpath("//a[@id='bowlers-t20s-tab']//following::div[contains(@class,'cb-col cb-col-100 text-bold cb-font-14 cb-rank-hdr cb-bg-grey text-center')]//following::div[contains(@class,'cb-col cb-col-100 cb-font-14 cb-lst-itm text-center')]")

l3=[]
for k in c:
    if k.text != '':
        l3.append(k.text.split("\n"))
print(l3, end=" ")


writer =pd.ExcelWriter('Bowlerrss.xlsx', engine ='xlsxwriter')

df=pd.DataFrame(l,columns=["position", "POW", "PROFILE", "player", "Rating"])
df.drop('POW',axis=1,inplace=True)
df.to_excel(writer,sheet_name='test', index = False )




df1=pd.DataFrame(l2,columns=["position", "POW", "PROFILE", "player", "Rating"])
df1.drop('POW',axis=1,inplace=True)
df1.to_excel(writer,sheet_name='odi', index = False )



df1=pd.DataFrame(l3,columns=["position", "POW", "PROFILE", "player", "Rating"])
df1.drop('POW',axis=1,inplace=True)
df1.to_excel(writer,sheet_name='T20', index = False )
writer.save()


writer.close()
driver.close()


# In[ ]:




