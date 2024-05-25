import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# set browser and get
myBrowser = webdriver.Chrome()
myBrowser.get('https://www.google.com')

# search element and input command
myBrowser.find_element(By.NAME, "q").send_keys("Dolar Hoje")
# open dollar search
myBrowser.find_element(By.NAME, "q").send_keys(Keys.RETURN)

# xpath
valueDollar = myBrowser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print('dolar:'+ valueDollar)

pyautogui.sleep(5)

