from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import urllib3
import string

Key_words = "spanish" #input("eneter key word: ")
links = []

urls = open("text_ex","w+")
http = urllib3.PoolManager()

search_area = "facebook"
area = "San Jose, CA" 
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