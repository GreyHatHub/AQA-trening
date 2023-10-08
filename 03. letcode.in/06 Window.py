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

link = 'https://letcode.in/windows'
driver.get(link)

#----- №1 Нажмите кнопку «Домой» 
try:
    driver.find_element(By.XPATH , '//*[@id="home"]').click()
    print('Тест №1 пройден')
except:
    print('ошибка №1')
    
#----- №2 Перейти на недавно открытую вкладку 
try:
    driver.switch_to.window(driver.window_handles[1])
    print('Тест №2 пройден')
except:
    print('ошибка №2')
    
#----- №3 Распечатать заголовок страницы 
try:
    print(driver.title.title())
    print('Тест №3 пройден')
except:
    print('ошибка №3')
#----- №4 Закройте родительское окно 
try:
    print('Тест №4 пройден')
except:
    print('ошибка №4')
#----- №5 Закройте дочернее окно 
try:
    driver.switch_to.window(driver.window_handles[1])
    print('Тест №5 пройден')
except:
    print('ошибка №5')
#----- №6 Нажмите кнопку «Несколько окон». 
try:
    driver.find_element(By.XPATH , '//*[@id="multi"]').click()
    print('Тест №6 пройден')
except:
    print('ошибка №6')

#----- №7 Распечатать весь заголовок окна 
try:
    driver.switch_to.window(driver.window_handles[1])
    print(driver.title.title())
    print('Тест №7 пройден')
except:
    print('ошибка №7')

#----- №8 Закройте все окна 
try:
    print('Тест №8 пройден')
except:
    print('ошибка №8')
time.sleep(5)
driver.quit()
