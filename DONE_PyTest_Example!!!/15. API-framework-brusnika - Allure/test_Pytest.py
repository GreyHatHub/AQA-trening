import pytest
import allure
import json
import warnings
import requests
warnings.filterwarnings('ignore')

##############################################################################
##############################################################################
##############################################################################

# Чтение данных из файла json
with open('UrlList.json', 'r') as file:
    templates = json.load(file)

##############################################################################
##############################################################################
##############################################################################

@allure.suite("Проверка метрик времени в Планировщике")
@allure.epic("Проверка запросов")
@allure.feature("Проверка метрики времени")
@pytest.mark.parametrize('case', templates['link'])
def test_api(api, param_factory, case):
    
    # установить заголовок тестового случая
    allure.dynamic.title(case['name'])
        
    # установка токена авторизации от системы
    headers = param_factory.Authorization(case["Auth"], templates["Auth"])
    
    # добавить описание в отчет
    if "description" in case:
        allure.dynamic.description(f"{case['description']}")
    
    # установка в Allure параметров
    allure.dynamic.parameter('Ссылка', case['url'])
    allure.dynamic.parameter('Метод', case['metod'])
    if "data" in case:
        allure.dynamic.parameter('Нагрузка', case['data'])
    
    #выполняеим апрос
    response = api.Query_Factory(case, headers, list(case['metod'].keys())[0])
    
    # with open('Response_0208.json', 'w', encoding='utf-8') as file:
    #     file.write(response[1].text)
    
    #выполняем тесты
    with allure.step(f'Код ответа {case["metod"].values()}'):
        allure.attach(bytes(str(response[1].headers), 'utf-8'), "Заголовок ответа")
        if len(response[1].text) < 20*1024*1024: # ограничение в 50 Мб за ответ
            allure.attach(response[1].text, "Тело ответа")
        else:
            allure.attach(f"{response[1].text.__len__()} байт", "Размер передаваемых данных")
        assert response[1].status_code == list(case['metod'].values())[0]
        
    with allure.step("Проверка времени загрузки"):
        assert response[0] > response[2] 
            
##############################################################################
##############################################################################
##############################################################################
if __name__ == "__main__":
    pytest.main(["-s", "-v"])
