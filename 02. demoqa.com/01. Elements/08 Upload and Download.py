import json
from selenium import webdriver
import time, requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import devtools as EK



chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')                   
chrome_options.page_load_strategy = 'eager'
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

url = 'https://demoqa.com/upload-download/'
driver.get(url)

##############################################################################
a = driver.find_element(By.XPATH, '//*[@id="downloadButton"]')
print( a.get_attribute("href"), ' --- ', a.get_attribute("download"))

##############################################################################
b = driver.find_element(By.CSS_SELECTOR , '#uploadFile')
b.send_keys("/home/otk/Documents/!Автотесты/Курсы по автотестам/DemoQA/Elements/New Empty File.txt")
print('\n\n', b.get_attribute('value'))

time.sleep(5)
driver.quit()
