import re
import sys
import time
import requests
import sqlite3
import logging
import subprocess
from subprocess import PIPE
from subprocess import Popen
from datetime import datetime

from bs4 import BeautifulSoup
from selenium import webdriver
from stem.util import system, term
from stem import process as tor_process
from fake_useragent import UserAgent
from elasticsearch import Elasticsearch as ES
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TorInit import TorInit

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

### test_code
class WallMarketCrawler(TorInit):

  def __init__(self, socks_port):
    #init tor proxy
    self.TorInit = TorInit(socks_port=socks_port)
    self.TorInit.startTorProxy()


  def crawlUrl(self):
    #crawl your web
    pass


if __name__ == '__main__':
  
  crawler = WallMarketCrawler(socks_port=9050)

