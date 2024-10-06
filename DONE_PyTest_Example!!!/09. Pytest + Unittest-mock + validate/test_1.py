import pytest
from unittest import mock

import requests
from jsonschema import validate


@pytest.fixture
def mocked_response():
    response_mock = mock.Mock()
    response_mock.json.return_value = {
        "result": {
            "name": "John",
            "age": 30
        }
    }
    response_mock.status_code = 200
    return response_mock

@pytest.mark.parametrize("expected_status_code", [200, 404, 500])
def test_api(expected_status_code, mocked_response):
    api_url = "https://example.com/api"

    #окаем метод запроса
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value = mocked_response

        # Отправляем запрос к API
        response = requests.get(api_url)

        # Проверяем код ответа
        # assert response.status_code == 200
        assert response.status_code == expected_status_code

        # Проверяем возвращаемые значения по схеме
        schema = {
            "type": "object",
            "properties": {
                "result": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                    },
                    "required": ["name", "age"],
                },
            },
            "required": ["result"],
        }
        validate(instance=response.json(), schema=schema)

        # Проверяем конкретные значения
        json_data = response.json()
        assert json_data["result"]["name"] == "John"
        assert json_data["result"]["age"] == 30

if __name__ == "__main__":
    pytest.main(["-s", "-v"])