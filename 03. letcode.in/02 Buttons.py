import json
from selenium import webdriver
import time
import random
from selenium.webdriver import ActionChains
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

link = 'https://letcode.in/buttons'
driver.get(link)

#----- №1
try:
    el = driver.find_element(By.XPATH , '//*[@id="home"]')
    time.sleep(1)
    el.click()
    time.sleep(1)
    driver.back()
    print('Тест №1 пройден')
except:
    print('ошибка №1')
    
#----- №2
try:
    el = driver.find_element(By.XPATH , '//*[@id="position"]')
    print(el.location)
    print('Тест №2 пройден')    
except:
    print('ошибка №2')

#----- №3
try:
    el = driver.find_element(By.XPATH , '//*[@id="color"]')
    print(el.value_of_css_property('background-color'))
    print('Тест №3 пройден')
except:
    print('ошибка №3')

#----- №4
try:
    el = driver.find_element(By.XPATH , '//*[@id="property"]')
    print(el.size)
    print('Тест №4 пройден')
except:
    print('ошибка №4')

#----- №5
try:
    el = driver.find_element(By.XPATH , '//button[contains(@class, "is-info")]')
    print(el.is_enabled())    
    print('Тест №5 пройден')
except:
    print('ошибка №5')

#----- №6
try:    
    el = driver.find_element(By.XPATH , '//*[contains(text(), "Button Hold!")]')
    action = ActionChains(driver)
    action.click_and_hold(el).perform()
    time.sleep(3)
    action.release().perform()
    print('Тест №6 пройден')
except:
    print('ошибка №6')

time.sleep(2)
driver.quit()
