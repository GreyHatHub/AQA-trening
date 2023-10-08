from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)


try:
    knopka=browser.find_element(By.CSS_SELECTOR, "button").click()
    confirm=browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)
    forma=browser.find_element(By.NAME,"text")
    forma.send_keys(y)
    sumbit=browser.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
