from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(webdriver.common.by.By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

try:
    input1 = browser.find_element(webdriver.common.by.By.ID, "answer")
    input1.send_keys(y)
    option1=browser.find_element(webdriver.common.by.By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(webdriver.common.by.By.ID, "robotsRule")
    option2.click()
    link=browser.find_element(webdriver.common.by.By.CSS_SELECTOR , "button.btn.btn-default")
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.quit()