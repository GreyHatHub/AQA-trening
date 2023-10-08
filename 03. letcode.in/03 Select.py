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

link = 'https://letcode.in/dropdowns'
driver.get(link)

#----- №1
try:
    driver.find_element(By.XPATH , '//*[@id="fruits"]').click()
    driver.find_element(By.XPATH , '//*[@value="0"]').click()
    print('Тест №1 пройден')
except:
    print('ошибка №1')
    
#----- №2
try:
    driver.find_element(By.XPATH , '//*[@value="aq"]').click()
    print('Тест №2 пройден')
except:
    print('ошибка №2')
#----- №3
try:
    driver.find_element(By.XPATH, '//*[@id="lang"]').click()
    k = driver.find_element(By.XPATH, '//*[@id="lang"]').find_elements(By.TAG_NAME, 'option')
    k[k.__len__()-1].click()
    print('Тест №3 пройден')
except:
    print('ошибка №3')
#----- №4
try:
    driver.find_element(By.XPATH, '//*[@id="country"]').click()
    k = driver.find_element(By.XPATH, '//*[@id="country"]').find_elements(By.TAG_NAME, 'option')
    for j in k:
        if j.text == 'India':
            j.click()    
    print('Тест №4 пройден')
except:
    print('ошибка №4')
    
# #----- №5
# try:
#     print('Тест №5 пройден')
# except:
#     print('ошибка №5')
# #----- №6
# try:
#     print('Тест №6 пройден')
# except:
#     print('ошибка №6')

time.sleep(5)
driver.quit()
