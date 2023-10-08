from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')           
chrome_options.add_argument("--start-maximized")       
chrome_options.page_load_strategy = 'eager'
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
driver = webdriver.Chrome(options=chrome_options)

link = 'https://demoqa.com/automation-practice-form/'
driver.get(link)

time.sleep(2)
driver.execute_script('document.getElementsByTagName("footer")[0].remove()')
driver.execute_script('document.getElementById("fixedban").remove()')


driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys("First")
driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys("First")
driver.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys("b@a.ru")


driver.find_element(By.XPATH,'//*[contains(text(), "Male")]').click()


driver.find_element(By.XPATH,'//*[@id="userNumber"]').send_keys("9789999999")


driver.find_element(By.CSS_SELECTOR,'#dateOfBirthInput').click()
Select(driver.find_element(By.XPATH,'//*[contains(@class, "year-select")]')).select_by_index(1)
Select(driver.find_element(By.XPATH,'//*[contains(@class, "month-select")]')).select_by_index(0)
driver.find_element(By.XPATH,'//*[contains(@class, "day--005")]').click()


subject = driver.find_element(By.ID,'subjectsInput')
subject.send_keys("a")
subject.send_keys(Keys.RETURN)


driver.find_element(By.XPATH,'//*[contains(text(), "Sports")]').click()


file = '/home/otk/Downloads/sampleFile.jpeg'
driver.find_element(By.CSS_SELECTOR ,'#uploadPicture').send_keys(file)


driver.find_element(By.XPATH,'//*[@id="currentAddress"]').send_keys("улица пушкина дом калатушкина")


driver.find_element(By.CSS_SELECTOR ,'#state').click()
driver.find_element(By.XPATH ,'//*[@id="react-select-3-option-1"]').click()
          

driver.find_element(By.CSS_SELECTOR ,'#city').click()
driver.find_element(By.XPATH ,'//*[@id="react-select-4-option-1"]').click()


driver.find_element(By.CSS_SELECTOR,'#submit').click()

time.sleep(5)
driver.quit()

