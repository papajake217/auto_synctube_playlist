from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import importlib
import random
from txtFileShuffler import shuffle

shuffle()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://sync-tube.de/create")
search = driver.find_element_by_class_name("searchInput")
file = open('links.txt', 'r')
with file as f:
    links = f.readlines()
links = [x.strip() for x in links]
numba = len(links)
for x in range (numba):
    search.send_keys(links[x])
    search.send_keys(Keys.RETURN)

