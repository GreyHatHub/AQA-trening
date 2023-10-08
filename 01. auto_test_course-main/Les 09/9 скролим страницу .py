from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

try:
    input1 = browser.find_element(By.ID ,"answer")
    input1.send_keys(y)
    option1=browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID ,"robotsRule")
    hello = "Hello"
    friends = " friends"
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    link=browser.find_element(By.TAG_NAME ,"button")
    browser.execute_script("return arguments[0].scrollIntoView(true);",link) 
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    # browser.quit()