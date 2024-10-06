import pytest
import allure

@allure.feature('Load page')
@allure.story('Code 200')
def test_get_locations_for_us_90210_check_status_code_equals_200(request_api):
    response = request_api.get("")
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"

@allure.feature('Load page')
@allure.story('Type content')
def test_get_locations_for_us_90210_check_content_type_equals_json(request_api):
      response = request_api.get("")
      with allure.step("Запрос отправлен, тип контента"):
          assert response.headers["Content-Type"] == "application/json"

@allure.feature('Body')
@allure.story('Check contry')
def test_get_locations_for_us_90210_check_country_equals_united_states(request_api):
      response = request_api.get("")
      response_body = response.json()
      with allure.step("Запрос отправлен, проверим страну"):
          assert response_body["country"] == "United States"
     
@allure.feature('Body')
@allure.story('Check place name')
def test_get_locations_for_us_90210_check_city_equals_beverly_hills(request_api):
      response = request_api.get("")
      response_body = response.json()
      with allure.step("Запрос отправлен, проверим улицу"):
          assert response_body["places"][0]["place name"] == "Beverly Hills"

@allure.feature('Body')
@allure.story('Check place')
def test_get_locations_for_us_90210_check_one_place_is_returned(request_api):
      response = request_api.get("")
      response_body = response.json()
      with allure.step("Запрос отправлен, проверим номер дома"):
          assert len(response_body["places"]) == 1


if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir", "./report", "-n", "auto"])
