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
    #--------Step №1-------
    url = 'https://demoqa.com/login/'
    driver.get(url)
    
    driver.find_element(By.ID, 'newUser').click()
    
    driver.find_element(By.ID, 'firstname').send_keys('Denis')
    driver.find_element(By.ID, 'lastname').send_keys('Lana')
    driver.find_element(By.ID, 'userName').send_keys('Den')
    driver.find_element(By.ID, 'password').send_keys('!1QazQazQaz#')
    time.sleep(2)
    CAPCHA = driver.find_element(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
    driver.switch_to.frame(CAPCHA)   
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'recaptcha-anchor'))).click()
    driver.switch_to.default_content()
    
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
    
    WebDriverWait(driver, "10").until(EC.alert_is_present())
    time.sleep(1)
    driver.switch_to.alert.accept()
    
    driver.find_element(By.ID, 'gotologin').click()
    driver.find_element(By.ID, 'userName').send_keys('Den')
    driver.find_element(By.ID, 'password').send_keys('!1QazQazQaz#')
    time.sleep(1)
    driver.find_element(By.ID, 'login').click() 
    
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(text(), "Delete Account")]').click()           
    print('\n',"Load complied")

except:
    print('!!!---ERRORE---!!!')
    time.sleep(5)
    driver.quit()
