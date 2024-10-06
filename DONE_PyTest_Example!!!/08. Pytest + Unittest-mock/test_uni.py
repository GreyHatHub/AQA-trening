import pytest
from unittest import mock
from myapi import MyAPI

@pytest.fixture
def mock_api_response():
    mock_response = mock.Mock()
    mock_response.json.return_value = {
        'id': 1,
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    }
    return mock_response

def test_api_get_user(mock_api_response):
    with mock.patch('myapi.requests.get') as mock_get:
        # Симулируем успешный ответ от API
        mock_get.return_value = mock_api_response

        # Инициализируем и вызываем метод API для получения пользователя
        api = MyAPI()
        user = api.get_user()
        
        # Проверяем, что полученные данные соответствуют ожидаемым
        assert user['id'] == 1
        assert user['name'] == 'John Doe'
        assert user['email'] == 'johndoe@example.com'
        assert mock_get.called

def test_api_create_user(mock_api_response):
    with mock.patch('myapi.requests.post') as mock_post:
        # Симулируем успешный ответ от API
        mock_post.return_value = mock_api_response

        # Инициализируем вызываем метод API для создания пользователя
        api = MyAPI()
        user_data = {
            'name': 'Jane Smith',
            'email': 'janesmith@example.com'
        }
        response = api.create_user(user_data)

        # Проверяем, что метод POST был вызван с правильными данными
        mock_post.assert_called_once_with(api.BASE_URL + '/users', json=user_data)

        # Проверяем, что полученный ответ содержит ожидаемые данные
        assert response['id'] == 1
        assert response['name'] == 'John Doe'
        assert response['email'] == 'johndoe@example.com'
