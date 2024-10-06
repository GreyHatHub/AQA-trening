import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver(request):
    # Создать экземпляр webdriver Firefox
    Firefox_options = webdriver.FirefoxOptions()
    Firefox_options.add_argument('--headless')  
    Firefox_options.page_load_strategy = 'eager'
    Firefox_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    driver = webdriver.Firefox(options=Firefox_options)
    
    def fin():
        # Закрыть браузер после завершения теста
        driver.quit()
    
    # Добавить функцию fin() в финализаторы, чтобы автоматически закрыть браузер после выполнения всех тестов
    request.addfinalizer(fin)
    
    return driver