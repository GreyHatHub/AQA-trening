import pytest
import requests
from jsonschema import validate

# Пример URL и схемы данных для тестирования
url = "http://example.com/api"

# Верная схема
schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}
# Неверная схема
schema1 = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"}
    },
    "required": ["id", "name"]
}

# Мок объект для эмуляции ответа от API
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

# Тестовая функция
@pytest.mark.parametrize("expected_status_code", [200, 404, 500])
@pytest.mark.parametrize("shema", [schema, schema1, schema])
def test_api(expected_status_code, shema):
    # Эмуляция ответа от API
    response_data = {"id": 1, "name": "Test"}
    response = MockResponse(response_data, 200)

    # Мок объект для эмуляции запроса к API
    def mock_get(url):
        return response

    # Замена оригинальной функции requests.get на мок объект
    requests.get = mock_get

    # Вызов и проверка кода ответа
    resp = requests.get(url)
    assert resp.status_code == 200

    # Проверка данных по схеме
    validate(instance=resp.json(), schema=shema)

    # Сравнение данных
    assert resp.json() == response_data
    

if __name__ == "__main__":
    pytest.main(["-s"])
