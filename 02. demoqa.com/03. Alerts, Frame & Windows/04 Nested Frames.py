import json
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import devtools as EK

# Подключаем Chrome
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')                   
chrome_options.page_load_strategy = 'eager'
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

# Подключаем Firefox
# Firefox_options = webdriver.FirefoxOptions()
# Firefox_options.add_argument('--headless')  
# Firefox_options.page_load_strategy = 'eager'
# Firefox_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
# driver = webdriver.Firefox(options=Firefox_options)


url = 'https://demoqa.com/nestedframes/'
driver.get(url)


# Играемся с фраймами
fr1 = driver.find_element(By.TAG_NAME,'iframe')
driver.switch_to.frame(fr1)
print(driver.find_element(By.TAG_NAME , 'body').text)


fr2 = driver.find_element(By.TAG_NAME,'iframe')
driver.switch_to.frame(fr2)
print('\n',driver.find_element(By.TAG_NAME , 'body').text)

driver.switch_to.default_content()
print('\n',driver.find_element(By.TAG_NAME , 'body').text)


time.sleep(2)
driver.quit()
