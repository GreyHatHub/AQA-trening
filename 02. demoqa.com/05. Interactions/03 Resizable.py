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

    url = 'https://demoqa.com/resizable/'
    driver.get(url)
    
    # Играемся с Resize
    El = driver.find_elements(By.CLASS_NAME, 'react-resizable-handle.react-resizable-handle-se')
    move = ActionChains(driver)
    time.sleep(2)
    move.click_and_hold(El[0]).move_by_offset(-50,-50).release().perform()    
    time.sleep(2)
    move.click_and_hold(El[0]).move_by_offset(350,150).release().perform() 
    
    # Играемся с Resize
    time.sleep(2)
    move.click_and_hold(El[1]).move_by_offset(-50,-50).release().perform()    
    time.sleep(2)
    move.click_and_hold(El[1]).move_by_offset(350,150).release().perform()    
    
    print('\n',"Load complied")
    time.sleep(2)
    driver.quit()
    
except:
    print('!!!---ERRORE---!!!')
    time.sleep(2)
    driver.quit()
