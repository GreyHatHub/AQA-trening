from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



link = 'https://demoqa.com/text-box/'
driver = webdriver.Chrome()
driver.get(link)

username = driver.find_element(By.XPATH , '//*[@id="userName"]')
email = driver.find_element(By.XPATH , '//*[@id="userEmail"]')
currentAddress = driver.find_element(By.XPATH , '//*[@id="currentAddress"]')
Addres = driver.find_element(By.XPATH , '//*[@id="permanentAddress"]')

username.send_keys("login")
email.send_keys("aaaa@mail.ru")
currentAddress.send_keys("passw")
Addres.send_keys("passw")

login_button = driver.find_element(By.XPATH,'//*[@id="submit"]')
login_button.click()

time.sleep(5)
driver.quit()
