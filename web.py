# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:42:53 2023

@author: Esraa
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

name_list=[]
link_list=[]
symmary_list=[]
row_list=[]
#import csv
driver=webdriver.Chrome("E:/tttt/chromedriver.exe")
base_url="https://search.lboro.ac.uk/s/search.html?collection=loughborough-courses"
for page in range(1, 372,10):
    # Construct the URL for the current page
    url = base_url + '&' + 'start_rank='+str(page) 

    # Open the website in Selenium-controlled Chrome
    driver.get(url)
    time.sleep(1)
    program_name_elements = driver.find_elements(By.CLASS_NAME,'result__heading')
    Symmary=driver.find_elements(By.CLASS_NAME,'result__summary')
    links =driver.find_elements(By.CLASS_NAME,'result__link')

    for name in  program_name_elements:
        name_list.append(name.text)
    for link in  links:
        link_list.append(link.get_attribute('title'))
    for sym in  Symmary:
        symmary_list.append(sym.text)
t_list=[]

for link in link_list:
    driver.get(link)
    program_type = driver.find_elements(By.CLASS_NAME,'site-header__title')
    if program_type[0].text=='Undergraduate study':
        program_type='Undergraduate study'
        program_duration = driver.find_elements(By.CLASS_NAME,'course-info__subheading')[0].text
        program_overview = driver.find_elements(By.CLASS_NAME,'text-overflow')[0].text
        program_requirements= driver.find_elements(By.CLASS_NAME,'entry-requirements__alerts')[0].text
        program_fees= driver.find_elements(By.CLASS_NAME,'course-fees-container')[0].text
    else:
        program_type='postgraduate study'
        program_duration='null'
        program_overview ='null'
        program_requirements=driver.find_elements(By.CLASS_NAME,'lead-paragraph--centred')[0].text
        program_fees=driver.find_elements(By.CLASS_NAME,'degree-fees-wrapper')[0].text

    q=link_list.index(link)
    row=[name_list[q],symmary_list[q],link,program_type,program_overview,program_duration,program_requirements,program_fees]
    row_list.append(row)   
print(len(row_list))



df = pd.DataFrame(row_list, columns=['name','symmary','link','program_type','program_overview','program_duration','program_requirements','program_fees'])

df.to_csv("E://data.csv", header=True, index=False)