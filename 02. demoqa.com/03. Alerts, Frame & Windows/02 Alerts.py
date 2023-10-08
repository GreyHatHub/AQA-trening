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


url = 'https://demoqa.com/alerts/'
driver.get(url)


# Играемся со Алертами
driver.find_element(By.CSS_SELECTOR , '#alertButton').click()
WebDriverWait(driver, "10").until(EC.alert_is_present())
time.sleep(2)
driver.switch_to.alert.accept()


driver.find_element(By.CSS_SELECTOR , '#timerAlertButton').click()
WebDriverWait(driver, "10").until(EC.alert_is_present())
time.sleep(2)
driver.switch_to.alert.accept()


driver.find_element(By.CSS_SELECTOR , '#confirmButton').click()
WebDriverWait(driver, "10").until(EC.alert_is_present())
time.sleep(2)
a = random.randint(1, 2)
if a == 1:
    driver.switch_to.alert.accept()
else: 
    driver.switch_to.alert.dismiss()


driver.find_element(By.CSS_SELECTOR , '#promtButton').click()
WebDriverWait(driver, "10").until(EC.alert_is_present())
time.sleep(2)
a = driver.switch_to.alert
a.send_keys("azaza")
time.sleep(2)
a.accept()

time.sleep(2)
driver.quit()
