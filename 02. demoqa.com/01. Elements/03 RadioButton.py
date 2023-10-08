from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



link = 'https://demoqa.com/radio-button/'
driver = webdriver.Chrome()
driver.get(link)

login_button = driver.find_element(By.XPATH,'//*[@for="yesRadio"]')
login_button.click()

time.sleep(5)
driver.quit()
