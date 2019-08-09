from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import urllib3
import string

import json

def searchGen(val, Site, Area):
    Key_words = str(val) #input("eneter key word: ")
    http = urllib3.PoolManager()

    search_area = str(Site)
    area = str(Area)
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/") #website to search through

    elem = driver.find_element_by_name("q")
    elem.send_keys(search_area + " " + Key_words + " " 'location: ' + area) #search through engine
    elem.send_keys(Keys.RETURN) #virtually enter the key

    Url = driver.current_url
    html_doc = http.request('GET', Url)
    soup = BeautifulSoup(html_doc.data, 'html')

    Soup_url = soup.find_all('a')
    print('done')
    print(" ")

    for link in Soup_url:
        if (link.find('https:') !=-1 and link.find("/url") !=-1 ):
            urls.write(link.get('href'))
            urls.write("%d\r\n")
            print(link.get('href'))

    print("complete")
    driver.close()
    return

def searchFB( val, Area):
    searchGen(val, "Facebook", Area)
    return

def search(val, Area):
    searchGen(val, " ", Area)
    return
    