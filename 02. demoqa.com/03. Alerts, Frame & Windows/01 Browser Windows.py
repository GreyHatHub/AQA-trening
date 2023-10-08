import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import devtools as EK

# Подключаем Chrome
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')                   
# chrome_options.page_load_strategy = 'eager'
# chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
# driver = webdriver.Chrome(options=chrome_options)

# Подключаем Firefox
Firefox_options = webdriver.FirefoxOptions()
# Firefox_options.add_argument('--headless')  
Firefox_options.page_load_strategy = 'eager'
Firefox_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Firefox(options=Firefox_options)


url = 'https://demoqa.com/browser-windows/'
driver.get(url)


# Играемся со вкладками
driver.find_element(By.CSS_SELECTOR , '#tabButton').click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.CSS_SELECTOR , '#sampleHeading').text)
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])


driver.find_element(By.CSS_SELECTOR , '#windowButton').click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.CSS_SELECTOR , '#sampleHeading').text)
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])


driver.find_element(By.CSS_SELECTOR , '#messageWindowButton').click()
driver.switch_to.window(driver.window_handles[1])
print(driver.find_element(By.TAG_NAME, 'body').text)
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])



time.sleep(2)
driver.quit()
