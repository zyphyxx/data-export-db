import time

from selenium import webdriver

web = webdriver.Chrome()

web.get('https://www.google.com/')

time.sleep(5)