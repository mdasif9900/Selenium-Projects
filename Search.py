from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os


if 'chromedriver.exe' in os.listdir():
    x = os.path.join(os.getcwd(), 'chromedriver.exe')
    print(x)
    driver = webdriver.Chrome(x)

else:
    print('Warning : chrome binaries missing! ')


def google(search):
    driver.get("https://www.google.com/")
    sleep(5)
    driver.find_element_by_xpath(
        r'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(search)
    sleep(2)
    driver.find_element_by_xpath(
        r'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.RETURN)


def duck(search):
    driver.get("https://duckduckgo.com/")
    sleep(5)
    driver.find_element_by_xpath(
        r'//*[@id="search_form_input_homepage"]').send_keys(search)
    sleep(2)
    driver.find_element_by_xpath(
        r'//*[@id="search_form_input_homepage"]').send_keys(Keys.RETURN)


def wiki(search):
    driver.get("https://www.wikipedia.org/")
    sleep(5)
    driver.find_element_by_xpath(r'//*[@id="searchInput"]').send_keys(search)
    sleep(2)
    driver.find_element_by_xpath(
        r'//*[@id="searchInput"]').send_keys(Keys.RETURN)


def bing(search):
    driver.get("https://www.bing.com/")
    sleep(5)
    driver.find_element_by_xpath(r'//*[@id="sb_form_q"]').send_keys(search)
    sleep(2)
    driver.find_element_by_xpath(
        r'//*[@id="sb_form_q"]').send_keys(Keys.RETURN)


search = input('what shouid i search? : ')
Search_engine = int(input('Where shouid i search ? \n 1.Google \t 2.DuckDuckGo \t 3.Wiki \t 4.Bing :'))
if Search_engine == 1:
    google(search)
elif Search_engine == 2:
    duck(search)
elif Search_engine == 3:
    wiki(search)
elif Search_engine == 4:
    bing(search)
else:
    google(search)
