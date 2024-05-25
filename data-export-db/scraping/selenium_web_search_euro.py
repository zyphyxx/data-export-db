import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# set browser and get
myBrowser = webdriver.Chrome()
myBrowser.get('https://www.google.com')

# search element and input command
myBrowser.find_element(By.NAME, "q").send_keys("Dolar Hoje")
pyautogui.sleep(1)

# open dollar search
myBrowser.find_element(By.NAME, "q").send_keys(Keys.RETURN)
pyautogui.sleep(1)

# xpath
valueDollar = \
myBrowser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
time.sleep(1)

print('dolar:', valueDollar)
pyautogui.sleep(1)

# -- EURO

# clear text input
myBrowser.find_element(By.NAME, "q").send_keys("")
pyautogui.sleep(1)

pyautogui.press('tab')
pyautogui.sleep(1)

pyautogui.press('enter')
pyautogui.sleep(1)

# search euro
myBrowser.find_element(By.NAME, "q").send_keys("euro")
pyautogui.sleep(1)

# open euro search
myBrowser.find_element(By.NAME, "q").send_keys(Keys.RETURN)
pyautogui.sleep(1)

# xpath
valueEuro = \
myBrowser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
pyautogui.sleep(1)

print('euro:', valueEuro)
