import pytest
from selenium import webdriver

def test_example(driver):
    # Открыть веб-страницу
    driver.get("https://old.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/zashchita-ot-virusa/")
    
    # Выполнить какие-то действия и проверки
    assert driver.title


if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir", "./report", "-n", "auto"])