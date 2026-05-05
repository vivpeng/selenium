from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

time.sleep(10)

driver.quit()