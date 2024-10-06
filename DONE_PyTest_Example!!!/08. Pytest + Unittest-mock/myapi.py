import requests

class MyAPI:
    BASE_URL = 'https://api.example.com'

    def get_user(self):
        response = requests.get(self.BASE_URL + '/users/1')
        return response.json()

    def create_user(self, user_data):
        response = requests.post(self.BASE_URL + '/users', json=user_data)
        return response.json()
