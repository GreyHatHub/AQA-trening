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


url = 'https://demoqa.com/auto-complete/'
driver.get(url)


# Играемся с модальными окнами
El = driver.find_element(By.ID, 'autoCompleteMultipleInput')
El.click()
El.send_keys("Gre")
El.send_keys(Keys.RETURN)

El.send_keys("Bl")
El.send_keys(Keys.RETURN)

El = driver.find_element(By.ID, 'autoCompleteSingleInput')
El.send_keys("Gre")
El.send_keys(Keys.RETURN)

time.sleep(2)
driver.quit()
