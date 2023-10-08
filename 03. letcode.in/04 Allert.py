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

link = 'https://letcode.in/alert'
driver.get(link)

#----- №1
try:
    driver.find_element(By.XPATH , '//*[@id="accept"]').click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    print('Тест №1 пройден')
    time.sleep(1)
except:
    print('ошибка №1')
    
#----- №2
try:
    driver.find_element(By.XPATH , '//*[@id="accept"]').click()
    time.sleep(1)
    a = driver.switch_to.alert
    print(a.text)
    a .dismiss()
    print('Тест №2 пройден')
    time.sleep(1)
except:
    print('ошибка №2')
#----- №3
try:
    driver.find_element(By.XPATH , '//*[@id="prompt"]').click()
    a = driver.switch_to.alert
    a.send_keys("ssssss")
    time.sleep(3)
    a.accept()
    print('Тест №3 пройден')
    time.sleep(1)
except:
    print('ошибка №3')
#----- №4
try:
    driver.find_element(By.XPATH , '//*[@id="modern"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH , '//button[contains(@class, "modal-close")]').click()  
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
