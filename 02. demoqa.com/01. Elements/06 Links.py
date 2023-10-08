import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import devtools as EK


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')                   
chrome_options.page_load_strategy = 'eager'
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

url = 'https://demoqa.com/links/'
driver.get(url)

# Играемся со вкладками
driver.find_element(By.XPATH , '//*[@id="simpleLink"]').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH , '//*[@id="dynamicLink"]').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)


#Играемся с JS
ID = ['//*[@id="created"]','//*[@id="moved"]','//*[@id="bad-request"]','//*[@id="bad-request"]','//*[@id="unauthorized"]','//*[@id="forbidden"]','//*[@id="invalid-url"]']
for l in ID:    
    a = driver.find_element(By.XPATH , l).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, l))).click()
    time.sleep(2)
    
    c = driver.find_element(By.XPATH , '//*[@id="linkResponse"]')
    print(l," --- ", c.text)

time.sleep(5)
driver.quit()
