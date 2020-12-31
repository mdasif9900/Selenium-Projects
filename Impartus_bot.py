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

driver.get("https://a.impartus.com/")
sleep(3)


def login(username, password):
    # login part
    driver.find_element_by_xpath(
        "//input[@name=\"username\"]").send_keys(username)
    driver.find_element_by_xpath(
        "//input[@name=\"password\"]").send_keys(password)
    driver.find_element_by_xpath(
        '/html/body/ui-view/div/div/ui-view/div/div[1]/form/div[2]/div').click()
    # end of login part


def im_search(search):
    # search
    driver.find_element_by_xpath(
        r'//*[@id="header"]/div[3]/input').send_keys(search)
    driver.find_element_by_xpath(
        r'//*[@id="header"]/div[3]/input').send_keys(Keys.RETURN)
    sleep(5)


username = input('Username : ')
password = input('Password : ')
login(username, password)
sleep(5)
im_search(input('what concept should i search : '))
