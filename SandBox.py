from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import urllib3
from urllib.request import urlopen

import string

import json
import re

def search(val, # Employment value that you want 
    Site,       # input any specific site, such as FB or other social sites
    Area):      # Search Area

    number = 0
    jsons = {}
    jsons[number] = []
    

    Key_words = str(val) 
    http = urllib3.PoolManager()

    search_area = str(Site)
    area = str(Area)
    driver = webdriver.Chrome('C:/Users/balto/OneDrive/Desktop/Tim&I business proj/CRM/chromedriver.exe')  # Optional argument, if not specified will search path.
    driver.get("https://www.google.com/") #website to search through

    elem = driver.find_element_by_name("q")
    elem.send_keys(search_area + " " + Key_words + " " 'location: ' + area) #search through engine
    elem.send_keys(Keys.RETURN) #virtually enter the key

    Url = driver.current_url
    html_doc = http.request('GET', Url)
    soup = BeautifulSoup((html_doc.data), 'html.parser')

    for link in soup.find_all('div',"kCrYT"):
        for urls in link.find_all('a'):
            #print(urls.get('href'))
            jsons[number] = {'link ' + str(number) : str(urls.get('href'))}
            number = number + 1
          
    jsonOut = json.dumps( jsons) #, sort_keys = True, indent = 4)
    
    print(jsonOut)
    #print(Links)
    print("complete")
    driver.close()
    return 

def searchFB( val,  # Employment value that you want 
    Area):          # Area of search
    search(val, "Facebook", Area)
    return

searchFB("Spanish", "San Jose")