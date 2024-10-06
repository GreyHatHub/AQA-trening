import requests
from hypothesis import given, strategies as st

BASE_URL = "https://jsonplaceholder.typicode.com"  # Пример URL для тестирования

# Тестирование GET метода
@given(st.integers(min_value=1, max_value=100))
def test_get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Тестирование POST метода
@given(title=st.text(), body=st.text(), user_id=st.integers(min_value=1, max_value=10))
def test_post_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == title
    assert response_data["body"] == body
    assert response_data["userId"] == user_id

# Тестирование PUT метода
@given(post_id=st.integers(min_value=1, max_value=100), title=st.text(), body=st.text())
def test_put_post(post_id, title, body):
    data = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == title
    assert response_data["body"] == body

# Тестирование PATCH метода
@given(post_id=st.integers(min_value=1, max_value=100), title=st.text())
def test_patch_post(post_id, title):
    data = {
        "title": title
    }
    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["title"] == title

# Тестирование DELETE метода
@given(post_id=st.integers(min_value=1, max_value=100))
def test_delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

# Для запуска тестов можно использовать команду pytest
if __name__ == "__main__":
    import pytest
    pytest.main()
