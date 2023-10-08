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

    url = 'https://demoqa.com/droppable/'
    driver.get(url)
    
    # Играемся
    El = driver.find_element(By.CLASS_NAME, 'drag-box.mt-4.ui-draggable.ui-draggable-handle')
    move = ActionChains(driver)
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(+200,0).release().perform()    

    time.sleep(2)
    driver.find_element(By.ID, 'droppableExample-tab-accept').click()
    El = driver.find_element(By.ID, 'acceptable')
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(+220,0).release().perform()  
    
    
    time.sleep(2)
    driver.find_element(By.ID, 'droppableExample-tab-preventPropogation').click()
    El = driver.find_element(By.ID, 'dragBox')
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(+220,+50).release().perform()  
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(0,+300).release().perform()  
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(0,-50).release().perform()
    
    time.sleep(2)
    driver.find_element(By.ID, 'droppableExample-tab-revertable').click()
    El = driver.find_element(By.ID, 'revertable')
    time.sleep(2)
    move.click_and_hold(El).move_by_offset(+220,+50).release().perform() 

    print('\n',"Load complied")
    time.sleep(2)
    driver.quit()
    
except:
    print('!!!---ERRORE---!!!')
    time.sleep(2)
    driver.quit()
