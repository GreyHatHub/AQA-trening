from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    element = driver.find_element(By.XPATH, "//input[@name='first_name']")
    element.send_keys("1")
    
    element = driver.find_element(By.XPATH, "//input[@name='last_name']")
    element.send_keys("2")
    
    element = driver.find_element(By.XPATH, "//input[contains(@class, 'city')]")
    element.send_keys("3")
    
    element = driver.find_element(By.XPATH, "//*[@id='country']")
    element.send_keys("4")    
    
    element = driver.find_element(By.XPATH, "//*[@id='submit_button']")
    element.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

