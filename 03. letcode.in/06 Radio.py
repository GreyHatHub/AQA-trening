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

link = 'https://letcode.in/radio'
driver.get(link)

X = driver.find_elements(By.CLASS_NAME , 'field')

#----- №1
try:
    driver.find_element(By.XPATH , '//*[@id="yes"]').click()
    print('Тест №1 пройден')
except:
    print('ошибка №1')
    
#----- №2
try:
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="two"]').click()
    print("Елемент №1 выделен? - ", driver.find_element(By.XPATH , '//*[@id="one"]').is_selected())
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="one"]').click()
    print("Елемент №2 выделен? - ", driver.find_element(By.XPATH , '//*[@id="two"]').is_selected())
    print('Тест №2 пройден')
except:
    print('ошибка №2')
    
#----- №3
try:
    driver.find_element(By.XPATH , '//*[@id="nobug"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH , '//*[@id="bug"]').click()
    if driver.find_element(By.XPATH , '//*[@id="nobug"]').is_selected():
        print('Ошибка - Елемент №1-выбран')
        print('Тест №3 пройден')
except:
    print('ошибка №3')
    
#----- №4
try:
    El = X[3].find_elements(By.TAG_NAME , 'input')
    for i in range(El.__len__()):
        if El[i].is_selected():
            print(f'Выбран элемент №{i+1}')
            print('Тест №4 пройден')
except:
    print('ошибка №4')
    
#----- №5
try:
    El = X[4].find_elements(By.TAG_NAME , 'input')
    for i in range(El.__len__()):
        if El[i].is_enabled() == False :
            print(f'Элемент №{i+1} отключен')
            print('Тест №5 пройден')
except:
    print('ошибка №5')
    
#----- №6
try:
    El = X[5].find_element(By.TAG_NAME , 'input')
    if El.is_selected() == True:
        print('Элемент выбран')
        print('Тест №6 пройден')
except:
    print('ошибка №6')

#----- №7
try:
    El = X[6].find_element(By.TAG_NAME , 'input')
    El.click()
    if El.is_selected() == True:
        print('Элемент выбран')        
        print('Тест №7 пройден')
except:
    print('ошибка №7')

time.sleep(5)
driver.quit()
