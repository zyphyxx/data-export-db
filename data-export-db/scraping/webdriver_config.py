import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="config/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

time.sleep(10)
driver.quit()

