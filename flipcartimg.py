import pandas as pd
import numpy as np
import requests
import urllib.parse
import pymysql.cursors
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import os
import time
import shutil

driver=webdriver.Chrome(executable_path=r"D:\11\chromedriver.exe")
driver.get("https://www.flipkart.com/womens-footwear/~womens-sandals/pr?sid=osp,iko&otracker=nmenu_sub_Women_0_Sandals")
html = driver.page_source
html = driver.execute_script("return document.documentElement.outerHTML;")
soup = BeautifulSoup(html, "html.parser")
target = soup.findAll("img")
# print(target)
imgfile=[]
for i in target:
    src=i.get("src")
    if src[0]=='h':
        print("hi")
        f=src[:-5]
        imgfile.append(f)
        print(f)
        
    else:
        pass
        
currentpath=os.getcwd()
for img in imgfile:
#     filename=img.split('/')[-1]
    file_name=os.path.basename(img)
   
    newpath=os.path.join(currentpath,"tt",file_name)
    urllib.request.urlretrieve(img,newpath)
#     file_name=os.path.basename(img)
