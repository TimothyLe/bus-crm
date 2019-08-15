
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html_page = urlopen("https://arstechnica.com")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    print (link.get('href'))