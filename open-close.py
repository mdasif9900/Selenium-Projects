from selenium import webdriver
import os

if 'chromedriver.exe' in os.listdir():
    # platform independent use os module
    x = os.path.join(os.getcwd(), 'chromedriver.exe')
    print(x)
    driver = webdriver.Chrome(x)

else:
    # if chrome driver is not found
    print('Warning : chrome binaries missing! ')


# open a url part
driver.get("https://www.google.com/")
driver.get("https://duckduckgo.com/")
driver.get("https://www.wikipedia.org/")

o = input('close it ? : ')
if o.lower()[0] == 'y':
    driver.close()
