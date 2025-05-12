import os
import requests
from dotenv import load_dotenv
 
load_dotenv()  # Carrega variáveis do .env
 
class ApiService:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
 
    def get(self, endpoint: str, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        return response
 
    def post(self, endpoint: str, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=json, headers=headers)
        return response
 
    def put(self, endpoint: str, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=json, headers=headers)
        return response
 
    def delete(self, endpoint: str, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response