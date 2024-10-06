import pytest
import requests
import allure
import json
import time

templates=[]
Cookie=[]
Token_monitor=[]
Token_proc=[]

class APIRequestFactory:
    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'GET request to: {url}'):
            return requests.get(url=url, params=params, headers=headers)
    def post(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'POST request to: {url}'):
            return requests.post(url=url, params=params, data=data, json=json, headers=headers)
    def put(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'PUT request to: {url}'):
            return requests.put(url=url, params=params, data=data, json=json, headers=headers)
    def patch(self, path="/", params=None, data=None, json=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'patch request to: {url}'):
            return requests.patch(url=url, params=params, data=data, json=json, headers=headers)
    def delete(self, path="/", params=None, headers=None):
        url = f"{self.base_address}{path}"
        with allure.step(f'DELETE request to: {url}'):
            return requests.delete(url=url, params=params, headers=headers)
    
    def Query_Factory(self, case=None, headers=None, metod=None):
        result=[]
        # установка дельты времени 
        page_load_delta = 10
        if "delta" in case:
            result.append(case["delta"]*1.05)
        else:
            result.append(page_load_delta)
            
        start_time = time.time()
        
        # выполнение запросов
        if  metod =='get':
            result.append(self.get(case['url'], None, headers))
        
        elif metod =='post':
            result.append(self.post(case['url'], None, None, case['data'], headers))
        
        elif metod =='put':
            result.append(self.put(case['url'], None, None, case['data'], headers))
        
        elif metod =='patch':
            result.append(self.patch(case['url'], None, None, case['data'], headers))
        
        elif metod =='delete':
            result.append(self.delete(case['url'], None, None, case['data'], headers))      
        
        end_time = time.time()
        page_load_time = end_time - start_time
        result.append(page_load_time)
        
        return result
    
@pytest.fixture
def api():
    return APIRequestFactory(base_address="")

##############################################################################
##############################################################################
##############################################################################

class ParamClass:
    def __init__(self, item, templates):
        self.item = item
        self.templates = templates
        
    def Authorization(self, item=None, templates=None):
        if item == "NoAuth":
            headers = {
                'Content-Type': 'application/json'
                }            
        elif item == "Token_monitor":
            Token_monitor = templates["Token_monitor"]
            headers = {
                'Host': 'process-monitor.brusnika.ru',
                'Token': Token_monitor,
                'Content-Type': 'application/json'
                }
        elif item =="Token_proc":
            Token_proc = templates["Token_proc"]
            headers = {
                'Host': 'erp-core.staging.brusnika.tech',
                'Authorization': f'Bearer {Token_proc}',
                'Content-Type': 'application/json'
                }
        elif item =="cookie":
            Cookie = templates["Cookie"]
            headers = {
                'Host': 'scheduler.brusnika.ru',
                'Cookie': Cookie,
                'Content-Type': 'application/json'
                }
        return headers

@pytest.fixture
def param_factory():
    return ParamClass(item={}, templates={})

##############################################################################
##############################################################################
##############################################################################




