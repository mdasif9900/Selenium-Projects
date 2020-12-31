from selenium import webdriver
import os


if 'chromedriver.exe' in os.listdir():
    x = os.path.join(os.getcwd(), 'chromedriver.exe')
    print(x)
    driver = webdriver.Chrome(x)
else:
    print('Warning : chrome binaries missing! ')


print(f'current window size is : {driver.get_window_size()}')

# maximize window
driver.maximize_window()
print(f'maximised window size is : {driver.get_window_size()}')

# set window size
driver.set_window_size(480, 320)
print(f'after resizing window size is : {driver.get_window_size()}')

# position control
x = int(input('X : '))
y = int(input('Y : '))
driver.set_window_position(x, y, windowHandle='current')
