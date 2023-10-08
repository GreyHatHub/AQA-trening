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

url = 'https://demoqa.com/broken/'
driver.get(url)


Element = driver.find_element(By.XPATH , '//div[contains(@class, "col-md-6")]/div[2]/img[1]')
a = requests.head(Element.get_attribute('src'))
json = a.headers
if 'image/jpeg' in json['Content-Type']:
    print (Element.get_attribute('src'), ' --- image/jpeg ', a.status_code)
else:
    print (Element.get_attribute('src'), ' --- text/html ', a.status_code)


Element = driver.find_element(By.XPATH , '//div[contains(@class, "col-md-6")]/div[2]/img[2]')
a = requests.head(Element.get_attribute('src'))
json = a.headers
if 'image/jpeg' in json['Content-Type']:
    print (Element.get_attribute('src'), ' --- image/jpeg ', a.status_code)
else:
    print (Element.get_attribute('src'), ' --- text/html ', a.status_code)


Element = driver.find_element(By.XPATH , '//*[contains(text(), "Click Here for Valid Link")]')
a = requests.head(Element.get_attribute('href'))
print (Element.get_attribute('href'), ' --- ', a.status_code)


Element = driver.find_element(By.XPATH , '//*[contains(text(), "Click Here for Broken Link")]')
a = requests.head(Element.get_attribute('href'))
print (Element.get_attribute('href'), ' --- ', a.status_code)

time.sleep(5)
driver.quit()
