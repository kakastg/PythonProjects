from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://allegro.pl/")
html = driver.page_source
soup = BeautifulSoup(html)
print(soup.prettify())
