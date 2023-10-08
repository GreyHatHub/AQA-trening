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


url = 'https://demoqa.com/select-menu/'
driver.get(url)

try:
    Combo = driver.find_elements(By.CLASS_NAME, 'css-19bqh2r')
    
    Combo[0].click()
    Value = driver.find_element(By.ID, 'react-select-2-input')
    Value.send_keys("a r")
    Value.send_keys(Keys.RETURN)
   
    Combo[1].click()
    Value = driver.find_element(By.ID, 'react-select-3-input')
    Value.send_keys("d")
    Value.send_keys(Keys.RETURN)
    
    m = driver.find_element(By.ID, 'oldSelectMenu')
    m.send_keys('m')
    m.send_keys(Keys.RETURN)
    
    Combo[2].click()
    Value = driver.find_element(By.ID, 'react-select-4-input')
    Value.send_keys("g")
    Value.send_keys(Keys.RETURN)
    Value.send_keys(Keys.ESCAPE)
    
    Value = driver.find_element(By.ID, 'cars').find_elements(By.TAG_NAME, 'option')
    Value[2].click()
    
    print('\n',"Load complied")
    
except:
    print('\n',"!!!---fail---!!!")
    # driver.quit()
