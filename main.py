from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://google.com")

# wait until the element "gLFyf" exists so it has time to load
# and the next line doesn't cause errors because it's not there
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# search
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("egg tarts" + Keys.ENTER)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Egg Tarts"))
)

# link to go to next page
# checking if that text is contained within a link tag (finds first thing)
# -> using LINK_TEXT to find if text exactly matches
# -> find_elements to find multiple
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Egg Tarts")

link.click()

time.sleep(20)

driver.quit()