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


url = 'https://demoqa.com/tabs/'
driver.get(url)

try:
    driver.find_element(By.ID, 'demo-tab-what').click()
    Tab =  driver.find_element(By.ID, 'demo-tabpane-what')
    print(Tab.text)
    
    driver.find_element(By.ID, 'demo-tab-origin').click()
    Tab =  driver.find_element(By.ID, 'demo-tabpane-origin')
    print('\n',Tab.text)
    
    driver.find_element(By.ID, 'demo-tab-use').click()
    Tab =  driver.find_element(By.ID, 'demo-tabpane-use')
    print('\n',Tab.text)
    
    mor = driver.find_element(By.ID, 'demo-tab-more')    
    driver.execute_script('arguments[0].removeAttribute("aria-disabled")', mor);
    driver.execute_script('arguments[0].setAttribute("class", "nav-item nav-link")', mor)
    mor.click()
    Tab =  driver.find_element(By.ID, 'demo-tabpane-more')
    print('\n',Tab.text)
    
    print('\n',"Load complied")
except:
    print('\n',"fail")
    time.sleep(2)
    driver.quit()
