from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    first_name=browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Vlad")
    last_name=browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Fara")
    email=browser.find_element(By.NAME, "email")
    email.send_keys("Fara@proger.ua")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Допустим ето етот док.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "input#file")
    element.send_keys(file_path)
    sumbit=browser.find_element(By.TAG_NAME, "button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
