import pytest
import allure
from selenium import webdriver
import os


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Ошибка при формировании скриншота')
                    return
            allure.attach(web_driver.get_full_page_screenshot_as_png(),
                          name='Error_Screenshot',
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print('Ошибка при формировании скриншота: {}'.format(e))
        if os.path.isfile('failures'):
            os.remove('./failures')


@pytest.fixture(scope="session")
def browser():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.page_load_strategy = 'eager'
    # chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    # driver = webdriver.Chrome(options=chrome_options)
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.page_load_strategy = 'eager'
    firefox_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    driver = webdriver.Firefox(options=firefox_options)

    driver.maximize_window()
    yield driver
    driver.quit()
