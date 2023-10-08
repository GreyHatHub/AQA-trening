from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



link = 'https://demoqa.com/webtables/'
driver = webdriver.Chrome()
driver.get(link)

#Step 1. Добавить строку 
driver.find_element(By.XPATH,'//*[@id="addNewRecordButton"]').click()

e = driver.find_element(By.XPATH,'//*[@id="firstName"]')
a = driver.find_element(By.XPATH,'//*[@id="lastName"]')
b = driver.find_element(By.XPATH,'//*[@id="userEmail"]')
c = driver.find_element(By.XPATH,'//*[@id="age"]')
d = driver.find_element(By.XPATH,'//*[@id="salary"]')
r = driver.find_element(By.XPATH,'//*[@id="department"]')

e.send_keys("firstName")
a.send_keys("lastName")
b.send_keys("aaa@mail.ru")
c.send_keys("23")
d.send_keys("32432523")
r.send_keys("deparasdasdrtment")

driver.find_element(By.XPATH,'//*[@id="submit"]').click()

#Step 2. Получаем данные со всей таблицы  и выводим добавленную строку
login_button = driver.find_elements(By.XPATH,'//*[@class="rt-tr-group"]')
print(login_button[3].text)

time.sleep(5)
driver.quit()
