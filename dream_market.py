import re
import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from TorInit import TorInit



r = request.get("http://"+domain+"/?category=117", cookies=cookies, headers=headers)


soup = BeautifulSoup(r.text, "html.parser")
result = soup.find_all("a",class_=re.compile("^productThumbImage"))
page_link = list()


for item in result:
  page_link.append(item['href'])

page_link = list(set(page_link))


print(page_link)






