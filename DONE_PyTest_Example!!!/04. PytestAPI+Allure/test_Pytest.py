import pytest
import allure
import random
import string

array = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

##############################################################################
###################################### GET  ##################################
##############################################################################

def test_GET_FULL(request_api):
    response = request_api.get(f"https://fakerestapi.azurewebsites.net/api/v1/Activities")
    with allure.step("Код ответа 200"):
        assert response.status_code == 200

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("id", [i for i in range(1, 2)])
def test_GET_PARAM(request_api, id):
    response = request_api.get(f"https://fakerestapi.azurewebsites.net/api/v1/Activities/{id}")
    with allure.step("Код ответа 200"):
        assert response.status_code == 200

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("parametr", [i for i in ['available', 'pending', 'sold']])
def test_GET_QUERY_v1(request_api, parametr):
    param = {"status": f"{parametr}"}
    response = request_api.get(f"https://petstore.swagger.io/v2/pet/findByStatus",param)
    with allure.step("Код ответа 200"):
        assert response.status_code == 200

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("u, p", [('string','string')])
def test_GET_QUERY_v2(request_api, u, p,):
    param = {"username": f"{u}", "password":f"{p}"}
    response = request_api.get(f"https://petstore.swagger.io/v2/user/login",param)
    with allure.step("Код ответа 200"):
        assert response.status_code == 200

##############################################################################
###################################### POST ##################################
##############################################################################

@pytest.mark.parametrize("Json", [({
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2023-10-16T21:44:06.736Z",
        "status": "placed",
        "complete": True
      })])
def test_POST_SEND_BODY(request_api, Json):
    response = request_api.post(f"https://petstore.swagger.io/v2/store/order", None, None, Json)
    with allure.step("Код ответа 200"):
        assert response.status_code == 200
        
    with allure.step("Проверка тела ответа"):    
        assert "id" in response.json()
        assert "petId" in response.json()
        assert "quantity" in response.json()
        assert "shipDate" in response.json()
        assert "status" in response.json()
        assert "complete" in response.json()

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("petId", [i for i in range(1, 2)])
@pytest.mark.parametrize("name", [(''.join(random.choice(array) for _ in range(8)),)])
@pytest.mark.parametrize("status", [(''.join(random.choice(array) for _ in range(8)),)])
def test_POST_SEND_PARAM_and_QUERY(request_api, petId, name, status):
    param = {"name": f"{name}", "status": f"{status}"}
    response = request_api.post(f"https://petstore.swagger.io/v2/pet/{petId}", param, None, None)
    with allure.step("Проверка кода ответа"):
        try:
            with allure.step("Код ответа 200"):
                assert response.status_code == 200
        except:
            with allure.step("Код ответа 404"):
                assert response.status_code == 404


##############################################################################
###################################### PUT  ##################################
##############################################################################

@pytest.mark.parametrize("Json", [({
"id": 0,
"category": {
  "id": 0,
  "name": "string"
},
"name": "doggie",
"photoUrls": [
  "string"
],
"tags": [
  {
    "id": 0,
    "name": "string"
  }
],
"status": "available"
      })])
def test_PUT_SEND_BODY(request_api,Json):
    response = request_api.put(f"https://petstore.swagger.io/v2/pet", None, None, Json)
    with allure.step("Проверка кода ответа"):
        with allure.step("Код ответа 200"):
            assert response.status_code == 200  
            
    with allure.step("Проверка тела ответа"):    
        assert "id" in response.json()
        assert "category" in response.json()
        assert "name" in response.json()

#-----------------------------------------------------------------------------

@pytest.mark.parametrize("username, Json", [('string', {
"id": 0,
"username": "string",
"firstName": "string",
"lastName": "string",
"email": "string",
"password": "string",
"phone": "string",
"userStatus": 0
      })])
def test_PUT_SEND_PARAM_and_BODY(request_api, username, Json):
    
    response = request_api.put(f"https://petstore.swagger.io/v2/user/{username}", None, None, Json)
    with allure.step("Проверка кода ответа"):
        with allure.step("Код ответа 200"):
            assert response.status_code == 200  
            
    with allure.step("Проверка тела ответа"):    
        assert "code" in response.json()
        assert "type" in response.json()
        assert "message" in response.json()


##############################################################################
##############################################################################
##############################################################################
if __name__ == "__main__":
    pytest.main(["-s", "-v"])
