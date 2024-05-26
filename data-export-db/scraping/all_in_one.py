import pyautogui
import xlsxwriter
import os
import time

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
    myBrowser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[
        0].text
time.sleep(1)

print('dolar:', valueDollar)
pyautogui.sleep(1)

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
    myBrowser.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[
        0].text
pyautogui.sleep(1)

print('euro:', valueEuro)

# excel

path = "D:\\PY-Projects\\data-export-db\\data-export-db\\scraping\\config\\euro e dollar.xlsx"

# workbook
workbook = xlsxwriter.Workbook(path)

worksheet = workbook.add_worksheet('euro e dollar')

dollar = valueDollar.replace(',', '.')
euro = valueEuro.replace(',', '.')

worksheet.write("A1", "Valor do Dollar")
worksheet.write("A2", float(dollar))
worksheet.write("B1", "Valor do Euro")
worksheet.write("B2", float(euro))

workbook.close()

os.startfile(path)
