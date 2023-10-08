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


url = 'https://demoqa.com/date-picker/'
driver.get(url)

# Играемся с модальными окнами
day = 26
ti = "13:00"

El = driver.find_element(By.ID, 'datePickerMonthYearInput')
El.click()
driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select').send_keys('2022')
driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select').send_keys('au')
driver.find_element(By.XPATH, f'//div[contains(@class, "react-datepicker__day--0{day}")]').click()



El = driver.find_element(By.ID, 'dateAndTimePickerInput')
El.click()
driver.find_element(By.CLASS_NAME , 'react-datepicker__year-read-view--down-arrow').click()
Y = driver.find_elements(By.CLASS_NAME , 'react-datepicker__year-option')
for dateelement in Y:
    date = dateelement.text
    if date == '2026':
        dateelement.click()
        break


driver.find_element(By.CLASS_NAME , 'react-datepicker__month-read-view--down-arrow').click()
M = driver.find_elements(By.CLASS_NAME , 'react-datepicker__month-option')
for dateelement in M:
    date = dateelement.text
    if date == 'June':
        dateelement.click()
        break

driver.find_element(By.XPATH, f'//div[contains(@class, "react-datepicker__day--0{day}")]').click()

T = driver.find_elements(By.CLASS_NAME, 'react-datepicker__time-list-item')
for a in T:
    if a.text == ti:
        a.click()
        break


time.sleep(2)
driver.quit()
