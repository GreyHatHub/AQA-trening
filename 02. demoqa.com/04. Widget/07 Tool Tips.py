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


url = 'https://demoqa.com/tool-tips/'
driver.get(url)

try:
    ToolTip = driver.find_element(By.ID, 'toolTipButton')
    ActionChains(driver).move_to_element(ToolTip).perform()
    ToolTip.click()
    mes = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME,'tooltip-inner')))
    print("1.",mes.text)
    
    ToolTip = driver.find_element(By.ID, 'toolTipTextField')
    ActionChains(driver).move_to_element(ToolTip).perform()
    ToolTip.click()
    mes = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME,'tooltip-inner')))
    print("2.",mes.text)    
    
    print('\n',"Load complied")
except:
    print('\n',"!!!---fail---!!!")
    driver.quit()
