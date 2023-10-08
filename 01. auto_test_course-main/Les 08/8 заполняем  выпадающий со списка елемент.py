from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
    sum = str(int(x)+int(y))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum)
    button = browser.find_element(By.CSS_SELECTOR , "button.btn")
    button.click()
finally:
    time.sleep(5)
#     browser.quit()