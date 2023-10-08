from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR,'#treasure')
x_element_atribyte = x_element.get_attribute("valuex")
print(x_element_atribyte)
x = x_element_atribyte
y = calc(x)
try:
    input1 = browser.find_element(By.ID ,"answer")
    input1.send_keys(y)
    option1=browser.find_element(By.ID ,"robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID ,"robotsRule")
    option2.click()
    link=browser.find_element(By.CSS_SELECTOR ,"button.btn.btn-default")
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.quit()