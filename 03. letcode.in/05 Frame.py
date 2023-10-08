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

link = 'https://letcode.in/frame'
driver.get(link)

#----- №1
    # for i in range(iframes.__len__()):
    #     print(iframes[i].get_attribute('outerHTML'))

try:
    driver.switch_to.frame('firstFr')
    print('Тест №1 пройден')
except:
    print('ошибка №1')
    
#----- №2
try:
    driver.find_element(By.XPATH , '//input[@name="fname"]').send_keys("A")
    print('Тест №2 пройден')
except:
    print('ошибка №2')
    
#----- №3
try:
    driver.find_element(By.XPATH , '//input[@name="lname"]').send_keys("B")
    print('Тест №3 пройден')
except:
    print('ошибка №3')
    
# ----- №4
try:
    iframes = driver.find_elements(By.TAG_NAME,'iframe')
    for i in range(iframes.__len__()):
        if 'has-background-white' in iframes[i].get_attribute('outerHTML'):
            driver.switch_to.frame(iframes[i])
    print('Тест №4 пройден')
except:
    print('ошибка №4')
    
#----- №5
try:
    driver.find_element(By.XPATH , '//input[@name="email"]').send_keys("a@a.com")    
    print('Тест №5 пройден')
except:
    print('ошибка №5')

#----- №6
try:
    driver.switch_to.default_content()
    print('Тест №6 пройден')
except:
    print('ошибка №6')

time.sleep(5)
driver.quit()
