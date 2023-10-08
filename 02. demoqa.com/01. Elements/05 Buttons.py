from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

link = 'https://demoqa.com/buttons'
driver = webdriver.Chrome()
driver.get(link)

#Step 1. Добавить строку 
DC = driver.find_element(By.XPATH,'//*[@id="doubleClickBtn"]')
ActionChains(driver).move_to_element(DC).perform() 
ActionChains(driver).double_click(DC).perform()

RC = driver.find_element(By.XPATH,'//*[@id="rightClickBtn"]')
ActionChains(driver).move_to_element(RC).perform() 
ActionChains(driver).context_click(RC).perform() 

C = driver.find_elements(By.XPATH,'//*[contains(text(), "Click Me")]')
# Var 1
# driver.find_element(By.XPATH,f'//*[@id="{C[2].get_attribute("id")}"]').click()
# Var 2
C[2].click()

time.sleep(5)
driver.quit()
