from fastapi import FastAPI
from fastapi.testclient import TestClient
import allure

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


@allure.feature('Load page')
@allure.story('Check text')
def test_read_text():
    response = client.get("/")
    with allure.step("Проверка сообщения"):
        assert response.json() == {"msg": "Hello World"}
        
        
@allure.feature('Load page')
@allure.story('Code 200')
def test_code():
    response = client.get("/")
    with allure.step("Проверка статус кода"):
        assert response.status_code == 201