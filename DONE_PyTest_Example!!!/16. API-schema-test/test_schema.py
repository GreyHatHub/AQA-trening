import pytest
import allure
import requests
from jsonschema import validate, ValidationError

# Определим схему
    # "array" - указывает, что значение должно быть массивом.
    # "object" - указывает, что значение должно быть объектом (то есть набором пар "ключ-значение").
    # "boolean" - указывает, что значение должно быть логическим (true или false).
    # "integer" - указывает, что значение должно быть целым числом.
    # "number" - указывает, что значение должно быть числом (может быть как целым, так и дробным).
    # "string" - указывает, что значение должно быть строкой.
    # "null" - указывает, что значение может быть только null.
    
schema = {
    "type": "object", #тип ответа
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name", "email"] # обязательные параметры
}





# Функция для получения ответа (например, из API)
def get_response():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")  # пример API
    allure.dynamic.parameter("Схема", schema)
    allure.attach(response.text, "Тело ответа")
    return response.json()

# Тест для проверки схемы
def test_response_schema():
    response_json = get_response()
    
    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        pytest.fail(f"Response schema is invalid: {e.message}")

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
