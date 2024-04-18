from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_stars_data = []

def new_scrape():
     soup = BeautifulSoup(browser.page_source, "html.parser")
     temp_list = []
     for table in soup.find_all('table', attrs = {'class','wikitable'}):
          for tr_tags in table[2]:
               for td_tags in soup.find_all('td'):
                    temp_list.append(td_tags)
     new_stars_data.append(temp_list)
               
new_scrape()

headers = ['Name','Constellation','Right Ascension','Declination','App mag','Distance','Spectral Type', 'Mass', 'Radius','discovery year']

stars_df = pd.DataFrame(new_stars_data, columns=headers)

stars_df.to_csv('updated_scraped_data.csv',index=True, index_label="id")