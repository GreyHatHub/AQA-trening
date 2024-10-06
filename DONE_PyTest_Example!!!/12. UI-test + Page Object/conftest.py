import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    Firefox_options = webdriver.FirefoxOptions()
    # Firefox_options.add_argument('--headless')  
    Firefox_options.page_load_strategy = 'eager'
    Firefox_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    driver = webdriver.Firefox(options=Firefox_options)
    yield driver
    driver.quit()
