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

try:

    url = 'https://demoqa.com/sortable/'
    driver.get(url)
    
    # Играемся с List
    El = driver.find_element(By.CLASS_NAME, 'vertical-list-container.mt-4').find_elements(By.CLASS_NAME, 'list-group-item.list-group-item-action')
    move = ActionChains(driver)
    step = El[0].size["height"]
    time.sleep(2)
    move.click_and_hold(El[2]).move_by_offset(0,1*step).release().perform()
    
    # Играемся с Grid
    driver.find_element(By.ID, 'demo-tab-grid').click()
    El = driver.find_element(By.CLASS_NAME, 'create-grid').find_elements(By.CLASS_NAME, 'list-group-item.list-group-item-action')
    move = ActionChains(driver)
    stepH = El[0].size["height"]
    stepW = El[0].size["width"]
    time.sleep(2)
    move.click_and_hold(El[0]).move_by_offset(1*stepW,1*stepH).release().perform()    
    
    print('\n',"Load complied")

except:
    print('!!!---ERRORE---!!!')
    time.sleep(5)
    driver.quit()
