from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



link = 'https://demoqa.com/checkbox/'
driver = webdriver.Chrome()
driver.get(link)

# # Step #1. Home open

driver.find_element(By.XPATH,'//button[contains(@class, "rct-collapse-btn")]').click()
driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[3]/span/button').click()
driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[3]/ol/li[1]/span/label/span[1]').click()


time.sleep(5)
driver.quit()
