# Data Extraction from the website
#https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")


def get_data():
    pass


driver = webdriver.Chrome( "./chromedriver path")
driver.set_window_size(1250, 740)
driver.set_window_position(0, 0)
driver.get("Website URL")

input("Press Enter To Continue...")
get_data()
film_name_tag = driver.find_elements(By.TAG_NAME, 'tag name')
movieCount = 0

for k in film_name_tag:
    while movieCount < 3:
        print(k.text)
        movieCount += 1
        break

